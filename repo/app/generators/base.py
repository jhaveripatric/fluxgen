"""
Base document generator with FluxGen branding and text wrapping utilities
"""
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether
)
from reportlab.lib.units import inch, mm
from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import logging

logger = logging.getLogger(__name__)

# Register Montserrat fonts
_fonts_dir = Path(__file__).parent.parent / 'static' / 'fonts'
_fonts_registered = False

def _register_fonts():
    """Register custom fonts with ReportLab (called once)"""
    global _fonts_registered
    if _fonts_registered:
        return

    try:
        montserrat_bold = _fonts_dir / 'Montserrat-Bold.ttf'
        montserrat_regular = _fonts_dir / 'Montserrat-Regular.ttf'
        montserrat_semibold = _fonts_dir / 'Montserrat-SemiBold.ttf'

        if montserrat_bold.exists():
            pdfmetrics.registerFont(TTFont('Montserrat-Bold', str(montserrat_bold)))
        if montserrat_regular.exists():
            pdfmetrics.registerFont(TTFont('Montserrat', str(montserrat_regular)))
        if montserrat_semibold.exists():
            pdfmetrics.registerFont(TTFont('Montserrat-SemiBold', str(montserrat_semibold)))

        _fonts_registered = True
        logger.info("Montserrat fonts registered successfully")
    except Exception as e:
        logger.warning(f"Could not register Montserrat fonts: {e}. Falling back to Helvetica.")

# Register fonts on module load
_register_fonts()


class BaseDocumentGenerator:
    """Base class for all FluxGen document generators with proper text wrapping"""

    # FluxGen brand colors (from official branding guide)
    PRIMARY = HexColor('#2C3E50')      # Dark blue-gray (primary brand color)
    COPPER = HexColor('#B87333')       # Copper/Bronze (accent color)
    SILVER = HexColor('#C0C0C0')       # Silver (text color)
    LIGHT_GRAY = HexColor('#F3F4F6')   # Light gray (backgrounds)
    WHITE = HexColor('#FFFFFF')
    BLACK = HexColor('#000000')

    # Legacy aliases for backward compatibility
    NAVY = PRIMARY
    ORANGE = COPPER
    GRAY = SILVER
    
    def __init__(self, database_manager, output_dir: Path):
        """Initialize the document generator"""
        self.db = database_manager
        self.output_dir = output_dir
        self.output_dir.mkdir(exist_ok=True)
        
        # Set up styles
        self.styles = getSampleStyleSheet()
        self._setup_custom_styles()
        
        # Document elements
        self.story = []
        
        # Company data (loaded once)
        self.company_info = self.db.get_company_info()
        
        # Logo paths (optimized versions for PDF use)
        _images_dir = Path(__file__).parent.parent / 'static' / 'images'
        _optimized_dir = _images_dir / 'optimized'

        # Optimized logos (preferred)
        self.logo_header_path = _optimized_dir / 'fluxgen-logo-full-header.png'      # 600x200 - for headers
        self.logo_cover_path = _optimized_dir / 'fluxgen-square-logo-cover.png'      # 400x400 - for cover pages
        self.logo_footer_path = _optimized_dir / 'fluxgen-logo-monogram-footer.png'  # 200x200 - for footers

        # Fallback to original logos if optimized not found
        self.logo_full_path = _images_dir / 'fluxgen-logo-full.png'
        self.logo_square_path = _images_dir / 'fluxgen-square-logo.png'
        self.logo_monogram_path = _images_dir / 'fluxgen-logo-monogram.png'
        
    def _setup_custom_styles(self):
        """Set up custom paragraph styles for FluxGen documents"""

        # Determine font availability (Montserrat preferred, Helvetica fallback)
        bold_font = 'Montserrat-Bold' if _fonts_registered else 'Helvetica-Bold'
        regular_font = 'Montserrat' if _fonts_registered else 'Helvetica'
        semibold_font = 'Montserrat-SemiBold' if _fonts_registered else 'Helvetica-Bold'

        # Title style
        self.styles.add(ParagraphStyle(
            'FluxGenTitle',
            parent=self.styles['Title'],
            fontSize=24,
            textColor=self.PRIMARY,
            spaceAfter=20,
            spaceBefore=10,
            alignment=TA_CENTER,
            fontName=bold_font
        ))

        # Heading 1 style
        self.styles.add(ParagraphStyle(
            'FluxGenHeading1',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=self.PRIMARY,
            spaceAfter=12,
            spaceBefore=16,
            fontName=bold_font
        ))

        # Heading 2 style
        self.styles.add(ParagraphStyle(
            'FluxGenHeading2',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=self.PRIMARY,
            spaceAfter=10,
            spaceBefore=14,
            fontName=semibold_font
        ))

        # Body text style
        self.styles.add(ParagraphStyle(
            'FluxGenBody',
            parent=self.styles['Normal'],
            fontSize=10,
            leading=14,
            textColor=self.BLACK,
            spaceAfter=6,
            spaceBefore=0,
            alignment=TA_JUSTIFY,
            fontName=regular_font
        ))

        # Table cell style for text wrapping
        self.styles.add(ParagraphStyle(
            'FluxGenTableCell',
            parent=self.styles['Normal'],
            fontSize=9,
            leading=12,
            textColor=self.BLACK,
            spaceAfter=0,
            spaceBefore=0,
            alignment=TA_LEFT,
            fontName=regular_font
        ))

        # Table header style
        self.styles.add(ParagraphStyle(
            'FluxGenTableHeader',
            parent=self.styles['Normal'],
            fontSize=10,
            leading=12,
            textColor=self.WHITE,
            spaceAfter=0,
            spaceBefore=0,
            alignment=TA_CENTER,
            fontName=bold_font
        ))
        
        # Small text style
        self.styles.add(ParagraphStyle(
            'FluxGenSmall',
            parent=self.styles['Normal'],
            fontSize=8,
            leading=10,
            textColor=self.SILVER,
            spaceAfter=3,
            spaceBefore=0,
            fontName=regular_font
        ))
    
    def create_wrapped_table_cell(self, text: str, style_name: str = 'FluxGenTableCell') -> Paragraph:
        """Create a Paragraph object for table cells to ensure text wrapping"""
        if text is None:
            text = ''
        return Paragraph(str(text), self.styles[style_name])
    
    def create_header_cell(self, text: str) -> Paragraph:
        """Create a header cell with proper styling"""
        return Paragraph(str(text), self.styles['FluxGenTableHeader'])
    
    def format_currency(self, amount: Optional[float], currency: str = 'CAD') -> str:
        """Format currency values"""
        if amount is None:
            return 'N/A'
        return f"{currency} ${amount:,.2f}"
    
    def format_date(self, date_str: Optional[str]) -> str:
        """Format date strings"""
        if not date_str:
            return 'N/A'
        try:
            # Handle different date formats
            if 'T' in date_str:
                date_obj = datetime.fromisoformat(date_str.replace('Z', '+00:00'))
            else:
                date_obj = datetime.fromisoformat(date_str)
            return date_obj.strftime('%B %d, %Y')
        except:
            return date_str
    
    def add_title(self, title: str):
        """Add a title to the document"""
        self.story.append(Paragraph(title, self.styles['FluxGenTitle']))
        self.story.append(Spacer(1, 0.3*inch))
    
    def add_heading1(self, heading: str):
        """Add a main heading"""
        self.story.append(Paragraph(heading, self.styles['FluxGenHeading1']))
    
    def add_heading2(self, heading: str):
        """Add a sub-heading"""
        self.story.append(Paragraph(heading, self.styles['FluxGenHeading2']))
    
    def add_body_text(self, text: str):
        """Add body text"""
        if text:
            self.story.append(Paragraph(text, self.styles['FluxGenBody']))
    
    def add_spacer(self, height: float = 0.2):
        """Add vertical spacing"""
        self.story.append(Spacer(1, height*inch))
    
    def add_page_break(self):
        """Add a page break"""
        self.story.append(PageBreak())
    
    def create_standard_table(self, data: List[List[str]], 
                            col_widths: List[float],
                            has_header: bool = True,
                            style_commands: Optional[List] = None) -> Table:
        """
        Create a properly formatted table with text wrapping
        
        Args:
            data: Table data as list of lists
            col_widths: Column widths in inches
            has_header: Whether first row is a header
            style_commands: Additional table style commands
        """
        if not data:
            return None
        
        # Convert all cells to Paragraph objects for text wrapping
        wrapped_data = []
        for i, row in enumerate(data):
            wrapped_row = []
            for cell in row:
                if i == 0 and has_header:
                    # Header row
                    wrapped_row.append(self.create_header_cell(cell))
                else:
                    # Data row
                    wrapped_row.append(self.create_wrapped_table_cell(cell))
            wrapped_data.append(wrapped_row)
        
        # Create table with page splitting enabled
        table = Table(
            wrapped_data, 
            colWidths=[w*inch for w in col_widths],
            repeatRows=1 if has_header else 0,
            splitByRow=True  # Enable splitting across pages
        )
        
        # Base table style
        table_style = [
            # Header styling (if applicable)
            ('BACKGROUND', (0, 0), (-1, 0 if has_header else -1), self.NAVY if has_header else self.WHITE),
            ('TEXTCOLOR', (0, 0), (-1, 0 if has_header else -1), self.WHITE if has_header else self.BLACK),
            
            # Data rows styling
            ('BACKGROUND', (0, 1 if has_header else 0), (-1, -1), self.WHITE),
            ('TEXTCOLOR', (0, 1 if has_header else 0), (-1, -1), self.BLACK),
            
            # Grid and borders
            ('GRID', (0, 0), (-1, -1), 0.5, self.GRAY),
            ('LINEBELOW', (0, 0), (-1, 0), 2, self.NAVY),
            
            # Alignment and padding
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('VALIGN', (0, 0), (-1, -1), 'TOP'),
            ('LEFTPADDING', (0, 0), (-1, -1), 8),
            ('RIGHTPADDING', (0, 0), (-1, -1), 8),
            ('TOPPADDING', (0, 0), (-1, -1), 6),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ]
        
        # Add alternating row colors for better readability
        if len(wrapped_data) > 1:
            start_row = 1 if has_header else 0
            for i in range(start_row, len(wrapped_data), 2):
                table_style.append(('BACKGROUND', (0, i), (-1, i), HexColor('#F9FAFB')))
        
        # Add custom style commands
        if style_commands:
            table_style.extend(style_commands)
        
        table.setStyle(TableStyle(table_style))
        return table
    
    def add_table(self, data: List[List[str]], 
                  col_widths: List[float],
                  has_header: bool = True,
                  title: Optional[str] = None,
                  style_commands: Optional[List] = None):
        """Add a table to the document with proper text wrapping"""
        
        if title:
            self.add_heading2(title)
        
        table = self.create_standard_table(data, col_widths, has_header, style_commands)
        if table:
            self.story.append(table)
            self.story.append(Spacer(1, 0.2*inch))
    
    def _create_logo_image(self, logo_type: str = 'header', width: float = None, max_height: float = None) -> Optional[Image]:
        """
        Create a ReportLab Image object for the logo with proper aspect ratio preservation.

        Args:
            logo_type: 'header' (horizontal), 'cover' (square with text), 'footer' (monogram only)
            width: Target width in inches (may be reduced to fit max_height while preserving aspect ratio)
            max_height: Maximum height in inches (logo will scale to fit while preserving aspect ratio)

        Returns:
            Image object or None if logo file not found
        """
        # Logo type configurations: (preferred_path, fallback_path, target_width, max_height)
        # The logo will be scaled to fit BOTH constraints while PRESERVING ASPECT RATIO
        # - For wide logos (header): max_height is the binding constraint
        # - For square logos (footer/cover): either can be binding
        logo_configs = {
            'header': (self.logo_header_path, self.logo_full_path, 3.5, 0.8),      # Horizontal banner
            'cover': (self.logo_cover_path, self.logo_square_path, 2.5, 2.5),      # Square for cover pages
            'footer': (self.logo_footer_path, self.logo_monogram_path, 0.4, 0.4),  # Monogram (square) for footer
            # Legacy support
            'full': (self.logo_header_path, self.logo_full_path, 3.5, 0.8),
            'monogram': (self.logo_footer_path, self.logo_monogram_path, 0.4, 0.4),
        }

        config = logo_configs.get(logo_type, logo_configs['header'])
        preferred_path, fallback_path, default_width, default_max_height = config

        # Use provided values or defaults
        target_width = width or default_width
        max_height = max_height or default_max_height

        # Try optimized logo first, then fallback
        logo_path = preferred_path if preferred_path.exists() else fallback_path

        if not logo_path.exists():
            logger.warning(f"Logo not found at {logo_path}")
            return None

        try:
            # Get actual image dimensions to calculate aspect ratio
            from PIL import Image as PILImage
            with PILImage.open(logo_path) as img:
                img_width, img_height = img.size
            aspect_ratio = img_width / img_height

            # Calculate dimensions that fit BOTH constraints while preserving aspect ratio
            # Option 1: Use target_width and calculate height
            calc_height_from_width = target_width / aspect_ratio
            # Option 2: Use max_height and calculate width
            calc_width_from_height = max_height * aspect_ratio

            # Choose the option that fits both constraints
            if calc_height_from_width <= max_height:
                # Width-constrained: use target_width, height will fit
                final_width = target_width
                final_height = calc_height_from_width
            else:
                # Height-constrained: use max_height, reduce width to maintain ratio
                final_width = calc_width_from_height
                final_height = max_height

            # Create image with calculated dimensions (preserving aspect ratio)
            logo = Image(str(logo_path), width=final_width*inch, height=final_height*inch)
            return logo

        except ImportError:
            # PIL not available, fall back to ReportLab's auto-scaling (width-only)
            logger.warning("PIL not available for aspect ratio calculation, using width-only scaling")
            logo = Image(str(logo_path), width=target_width*inch)
            return logo
        except Exception as e:
            logger.error(f"Error loading logo: {str(e)}")
            return None
    
    def add_cover_page_logo(self, width: float = 3.0):
        """
        Add centered square logo to cover page

        Args:
            width: Logo width in inches (default 3.0 for cover pages)
        """
        logo = self._create_logo_image('cover', width=width, max_height=3.0)
        if logo:
            logo.hAlign = 'CENTER'
            self.story.append(logo)
            self.story.append(Spacer(1, 0.5*inch))
    
    def add_company_header(self, include_logo: bool = True, logo_width: float = 2.5):
        """Add standard company header to document with optional logo

        Args:
            include_logo: Whether to include logo in header
            logo_width: Width of logo in header (in inches)
        """
        # Determine fonts
        bold_font = 'Montserrat-Bold' if _fonts_registered else 'Helvetica-Bold'
        regular_font = 'Montserrat' if _fonts_registered else 'Helvetica'

        if self.company_info:
            if include_logo:
                # Header with horizontal logo on left, company info on right
                logo = self._create_logo_image('header', width=logo_width)

                if logo:
                    # Create company info as Paragraphs for better formatting
                    company_name = Paragraph(
                        self.company_info.get('legal_name', 'FluxGen Industries Ltd.'),
                        ParagraphStyle(
                            'HeaderName',
                            parent=self.styles['Normal'],
                            fontSize=14,
                            textColor=self.PRIMARY,
                            fontName=bold_font,
                            alignment=TA_LEFT
                        )
                    )

                    tagline = Paragraph(
                        self.company_info.get('tagline', 'Forging Tomorrow\'s Welds'),
                        ParagraphStyle(
                            'HeaderTagline',
                            parent=self.styles['Normal'],
                            fontSize=11,
                            textColor=self.COPPER,
                            fontName=regular_font,
                            alignment=TA_LEFT
                        )
                    )

                    location = Paragraph(
                        f"{self.company_info.get('location', 'Airdrie')}, {self.company_info.get('province', 'Alberta')}, {self.company_info.get('country', 'Canada')}",
                        ParagraphStyle(
                            'HeaderLocation',
                            parent=self.styles['Normal'],
                            fontSize=9,
                            textColor=self.BLACK,
                            fontName=regular_font,
                            alignment=TA_LEFT
                        )
                    )

                    website = Paragraph(
                        self.company_info.get('website', 'www.fluxgen.ca'),
                        ParagraphStyle(
                            'HeaderWebsite',
                            parent=self.styles['Normal'],
                            fontSize=9,
                            textColor=self.BLACK,
                            fontName=regular_font,
                            alignment=TA_LEFT
                        )
                    )

                    # LINE 470-491: Header layout - Logo LEFT, Text RIGHT
                    # Create nested table for company info
                    info_data = [[company_name], [tagline], [location], [website]]
                    info_table = Table(info_data, colWidths=[4.0*inch], splitByRow=True)
                    info_table.setStyle(TableStyle([
                        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 15),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                        ('TOPPADDING', (0, 0), (-1, -1), 2),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
                    ]))

                    # Main header table: Logo (left) | Company Info (right)
                    # Logo is aspect-ratio preserved, so allocate space based on max logo width + padding
                    # Header logo (512x200) at 0.8" height = ~2.05" width, give it 2.5" column
                    header_data = [[logo, info_table]]
                    header_table = Table(header_data, colWidths=[2.5*inch, 4.0*inch], splitByRow=True)
                    header_table.setStyle(TableStyle([
                        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                        ('LEFTPADDING', (0, 0), (-1, -1), 0),
                        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
                        ('TOPPADDING', (0, 0), (-1, -1), 0),
                        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
                    ]))

                    self.story.append(header_table)
                    self.story.append(Spacer(1, 0.3*inch))

                    # Add horizontal line separator with brand color
                    line_table = Table([['']], colWidths=[6.5*inch], splitByRow=True)
                    line_table.setStyle(TableStyle([
                        ('LINEABOVE', (0, 0), (-1, 0), 2, self.PRIMARY),
                    ]))
                    self.story.append(line_table)
                    self.story.append(Spacer(1, 0.2*inch))
                    return

            # Fallback: header without logo (centered text)
            company_data = [
                [self.company_info.get('legal_name', 'FluxGen Industries Ltd.')],
                [self.company_info.get('tagline', 'Forging Tomorrow\'s Welds')],
                [f"{self.company_info.get('location', 'Airdrie')}, {self.company_info.get('province', 'Alberta')}, {self.company_info.get('country', 'Canada')}"],
                [self.company_info.get('website', 'www.fluxgen.ca')]
            ]

            header_table = Table(company_data, colWidths=[6.5*inch], splitByRow=True)
            header_style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (0, 0), bold_font),
                ('FONTSIZE', (0, 0), (0, 0), 16),
                ('FONTNAME', (0, 1), (0, 1), regular_font),
                ('FONTSIZE', (0, 1), (0, 1), 12),
                ('FONTNAME', (0, 2), (-1, -1), regular_font),
                ('FONTSIZE', (0, 2), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, 0), self.PRIMARY),
                ('TEXTCOLOR', (0, 1), (0, 1), self.COPPER),
                ('SPACEAFTER', (0, 0), (-1, -1), 6),
            ])
            header_table.setStyle(header_style)
            
            self.story.append(header_table)
            self.story.append(Spacer(1, 0.5*inch))
    
    def add_footer_info(self, include_logo: bool = True):
        """Add standard footer bar with PRIMARY background, logo LEFT, text RIGHT

        Args:
            include_logo: Whether to include the monogram logo in footer

        LINE 532-580: Footer layout configuration
        """
        self.story.append(Spacer(1, 0.3*inch))

        footer_text = f"Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')} | FluxGen Industries Ltd."

        # Determine font for footer text
        regular_font = 'Montserrat' if _fonts_registered else 'Helvetica'

        if include_logo:
            logo = self._create_logo_image('footer', width=0.45, max_height=0.45)
            if logo:
                # Footer text style - white text for dark background
                footer_style = ParagraphStyle(
                    'FooterText',
                    parent=self.styles['Normal'],
                    fontSize=8,
                    leading=10,
                    textColor=self.SILVER,
                    fontName=regular_font,
                    alignment=TA_LEFT
                )
                footer_para = Paragraph(footer_text, footer_style)

                # LINE 560-575: Footer bar layout - Logo (left) | Text (right)
                # Adjust column widths here (logo_col + text_col = 6.5 inches total)
                footer_data = [[logo, footer_para]]
                footer_table = Table(footer_data, colWidths=[0.7*inch, 5.8*inch], splitByRow=True)
                footer_table.setStyle(TableStyle([
                    # Dark PRIMARY background
                    ('BACKGROUND', (0, 0), (-1, -1), self.PRIMARY),
                    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                    ('LEFTPADDING', (0, 0), (0, 0), 10),   # Logo padding
                    ('LEFTPADDING', (1, 0), (1, 0), 10),   # Text padding
                    ('RIGHTPADDING', (0, 0), (-1, -1), 10),
                    ('TOPPADDING', (0, 0), (-1, -1), 8),
                    ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
                ]))
                self.story.append(footer_table)
                return

        # Fallback: footer without logo (still with dark background)
        footer_style = ParagraphStyle(
            'FooterTextOnly',
            parent=self.styles['Normal'],
            fontSize=8,
            textColor=self.SILVER,
            fontName=regular_font,
        )
        fallback_table = Table([[Paragraph(footer_text, footer_style)]], colWidths=[6.5*inch])
        fallback_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, -1), self.PRIMARY),
            ('LEFTPADDING', (0, 0), (-1, -1), 10),
            ('TOPPADDING', (0, 0), (-1, -1), 8),
            ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ]))
        self.story.append(fallback_table)
    
    def generate_document(self, filename: str, title: str = None) -> Path:
        """
        Generate the PDF document
        
        Args:
            filename: Output filename (without extension)
            title: Document title (optional)
        
        Returns:
            Path to generated PDF file
        """
        # Ensure filename has .pdf extension
        if not filename.endswith('.pdf'):
            filename += '.pdf'
        
        output_path = self.output_dir / filename
        
        # Create document
        doc = SimpleDocTemplate(
            str(output_path),
            pagesize=letter,
            rightMargin=1*inch,
            leftMargin=1*inch,
            topMargin=1*inch,
            bottomMargin=1*inch,
            title=title or filename
        )
        
        try:
            # Build the document
            doc.build(self.story)
            logger.info(f"Document generated successfully: {output_path}")
            return output_path
            
        except Exception as e:
            logger.error(f"Error generating document {filename}: {str(e)}")
            raise
    
    def build_content(self):
        """
        Abstract method to be implemented by subclasses
        This method should build the document content into self.story
        """
        raise NotImplementedError("Subclasses must implement build_content method")