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
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any, Optional, Tuple
import logging

logger = logging.getLogger(__name__)


class BaseDocumentGenerator:
    """Base class for all FluxGen document generators with proper text wrapping"""
    
    # FluxGen brand colors
    NAVY = HexColor('#1F3A4A')
    ORANGE = HexColor('#C87533') 
    GRAY = HexColor('#6B7280')
    LIGHT_GRAY = HexColor('#F3F4F6')
    WHITE = HexColor('#FFFFFF')
    BLACK = HexColor('#000000')
    
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
        
    def _setup_custom_styles(self):
        """Set up custom paragraph styles for FluxGen documents"""
        
        # Title style
        self.styles.add(ParagraphStyle(
            'FluxGenTitle',
            parent=self.styles['Title'],
            fontSize=24,
            textColor=self.NAVY,
            spaceAfter=20,
            spaceBefore=10,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Heading 1 style
        self.styles.add(ParagraphStyle(
            'FluxGenHeading1',
            parent=self.styles['Heading1'],
            fontSize=16,
            textColor=self.NAVY,
            spaceAfter=12,
            spaceBefore=16,
            fontName='Helvetica-Bold'
        ))
        
        # Heading 2 style
        self.styles.add(ParagraphStyle(
            'FluxGenHeading2',
            parent=self.styles['Heading2'],
            fontSize=14,
            textColor=self.NAVY,
            spaceAfter=10,
            spaceBefore=14,
            fontName='Helvetica-Bold'
        ))
        
        # Body text style
        self.styles.add(ParagraphStyle(
            'FluxGenBody',
            parent=self.styles['Normal'],
            fontSize=10,
            leading=12,
            textColor=self.BLACK,
            spaceAfter=6,
            spaceBefore=0,
            alignment=TA_JUSTIFY,
            fontName='Helvetica'
        ))
        
        # Table cell style for text wrapping
        self.styles.add(ParagraphStyle(
            'FluxGenTableCell',
            parent=self.styles['Normal'],
            fontSize=9,
            leading=11,
            textColor=self.BLACK,
            spaceAfter=0,
            spaceBefore=0,
            alignment=TA_LEFT,
            fontName='Helvetica'
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
            fontName='Helvetica-Bold'
        ))
        
        # Small text style
        self.styles.add(ParagraphStyle(
            'FluxGenSmall',
            parent=self.styles['Normal'],
            fontSize=8,
            leading=10,
            textColor=self.GRAY,
            spaceAfter=3,
            spaceBefore=0,
            fontName='Helvetica'
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
        
        # Create table
        table = Table(wrapped_data, colWidths=[w*inch for w in col_widths])
        
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
    
    def add_company_header(self):
        """Add standard company header to document"""
        if self.company_info:
            company_data = [
                [self.company_info.get('legal_name', 'FluxGen Industries Ltd.')],
                [self.company_info.get('tagline', 'Forging Tomorrow\'s Welds')],
                [f"{self.company_info.get('location', 'Airdrie')}, {self.company_info.get('province', 'Alberta')}, {self.company_info.get('country', 'Canada')}"],
                [self.company_info.get('website', 'www.fluxgen.ca')]
            ]
            
            header_table = Table(company_data, colWidths=[7*inch])
            header_style = TableStyle([
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (0, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (0, 0), 16),
                ('FONTNAME', (0, 1), (0, 1), 'Helvetica'),
                ('FONTSIZE', (0, 1), (0, 1), 12),
                ('FONTNAME', (0, 2), (-1, -1), 'Helvetica'),
                ('FONTSIZE', (0, 2), (-1, -1), 10),
                ('TEXTCOLOR', (0, 0), (0, 0), self.NAVY),
                ('TEXTCOLOR', (0, 1), (0, 1), self.ORANGE),
                ('SPACEAFTER', (0, 0), (-1, -1), 6),
            ])
            header_table.setStyle(header_style)
            
            self.story.append(header_table)
            self.story.append(Spacer(1, 0.5*inch))
    
    def add_footer_info(self):
        """Add standard footer information"""
        footer_text = f"Generated on {datetime.now().strftime('%B %d, %Y at %I:%M %p')} | FluxGen Industries Ltd."
        self.story.append(Spacer(1, 0.3*inch))
        self.story.append(Paragraph(footer_text, self.styles['FluxGenSmall']))
    
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