// FluxGen Documents JavaScript

class DocumentManager {
    constructor() {
        this.documents = [
            'executive_summary',
            'business_plan',
            'financial_projections',
            'market_analysis',
            'technical_specs',
            'team_bios',
            'site_requirements',
            'pitch_deck',
            'individual_prep'
        ];
        this.generatedFiles = [];
        this.init();
    }

    init() {
        this.setupEventHandlers();
        this.loadGeneratedFiles();
    }

    setupEventHandlers() {
        // Individual document generation buttons
        document.querySelectorAll('.generate-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const card = e.target.closest('.document-card');
                const docType = card.dataset.doc;
                this.generateDocument(docType);
            });
        });

        // Download buttons
        document.querySelectorAll('.download-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const card = e.target.closest('.document-card');
                const docType = card.dataset.doc;
                this.downloadDocument(docType);
            });
        });

        // Generate all button
        const generateAllBtn = document.getElementById('generate-all-btn');
        if (generateAllBtn) {
            generateAllBtn.addEventListener('click', () => this.generateAllDocuments());
        }

        // Progress modal close button
        const progressClose = document.getElementById('progress-close');
        if (progressClose) {
            progressClose.addEventListener('click', () => this.hideProgressModal());
        }
    }

    async loadGeneratedFiles() {
        try {
            const response = await FluxGen.api.get('/documents/list');
            this.generatedFiles = response.files || [];
            this.updateDocumentStates();
            this.updateFilesList();
        } catch (error) {
            console.error('Error loading generated files:', error);
            FluxGen.ui.showFlashMessage(`Error loading document list: ${error.message}`, 'error');
        }
    }

    updateDocumentStates() {
        this.documents.forEach(docType => {
            const card = document.querySelector(`[data-doc="${docType}"]`);
            if (!card) return;

            // Handle both underscore and hyphenated status IDs
            const statusEl = card.querySelector(`#${docType}-status`) || card.querySelector(`#${docType.replace('_', '-')}-status`);
            const downloadBtn = card.querySelector('.download-btn');

            // Guard against missing elements
            if (!statusEl || !downloadBtn) return;

            // Find the latest file for this document type using extractDocType for accuracy
            const docFiles = this.generatedFiles.filter(file => {
                const extractedType = this.extractDocType(file.filename);
                return extractedType === docType;
            }).sort((a, b) => new Date(b.modified) - new Date(a.modified));

            if (docFiles.length > 0) {
                const latestFile = docFiles[0];
                const count = docFiles.length;
                const countText = count > 1 ? ` (${count} files)` : '';
                statusEl.textContent = `Generated ${FluxGen.ui.formatDateTime(latestFile.modified)}${countText}`;
                statusEl.className = 'text-xs text-green-600';

                downloadBtn.disabled = false;
                downloadBtn.className = 'px-3 py-2 bg-fluxgen-orange text-white rounded text-sm hover:bg-opacity-90 transition-colors';
                downloadBtn.dataset.filename = latestFile.filename;
            } else {
                statusEl.textContent = 'Ready to generate';
                statusEl.className = 'text-xs text-gray-500';

                downloadBtn.disabled = true;
                downloadBtn.className = 'px-3 py-2 bg-gray-300 text-gray-500 rounded text-sm cursor-not-allowed';
                downloadBtn.removeAttribute('data-filename');
            }
        });
    }

    updateFilesList() {
        const filesList = document.getElementById('files-list');
        if (!filesList) return;

        if (this.generatedFiles.length === 0) {
            filesList.innerHTML = '<p class="text-gray-500">No documents generated yet.</p>';
            return;
        }

        // Sort files by modification date (newest first)
        const sortedFiles = [...this.generatedFiles].sort((a, b) => 
            new Date(b.modified) - new Date(a.modified)
        );

        const filesHTML = sortedFiles.map(file => {
            const docType = this.extractDocType(file.filename);
            const docTitle = this.getDocumentTitle(docType);
            
            return `
                <div class="flex items-center justify-between py-3 px-4 border border-gray-200 rounded-lg mb-2">
                    <div class="flex-1">
                        <div class="flex items-center">
                            <svg class="h-5 w-5 text-red-500 mr-3" fill="currentColor" viewBox="0 0 20 20">
                                <path fill-rule="evenodd" d="M4 4a2 2 0 012-2h4.586A2 2 0 0112 2.586L15.414 6A2 2 0 0116 7.414V16a2 2 0 01-2 2H6a2 2 0 01-2-2V4z" clip-rule="evenodd"/>
                            </svg>
                            <div>
                                <div class="font-medium text-gray-900">${docTitle}</div>
                                <div class="text-sm text-gray-500">
                                    ${FluxGen.ui.formatDateTime(file.modified)} • ${FluxGen.ui.formatFileSize(file.size)}
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="flex space-x-2">
                        <button onclick="documentManager.downloadFile('${file.filename}')" 
                                class="px-3 py-1 text-sm bg-fluxgen-orange text-white rounded hover:bg-opacity-90 transition-colors">
                            Download
                        </button>
                        <button onclick="documentManager.deleteFile('${file.filename}')" 
                                class="px-3 py-1 text-sm bg-red-600 text-white rounded hover:bg-red-700 transition-colors">
                            Delete
                        </button>
                    </div>
                </div>
            `;
        }).join('');

        filesList.innerHTML = filesHTML;
    }

    async generateDocument(docType) {
        const card = document.querySelector(`[data-doc="${docType}"]`);
        const generateBtn = card.querySelector('.generate-btn');
        const statusEl = card.querySelector(`#${docType}-status`) || card.querySelector(`#${docType.replace('_', '-')}-status`);

        try {
            FluxGen.ui.showLoading(generateBtn, true);
            statusEl.textContent = 'Generating...';
            statusEl.className = 'text-xs text-blue-600';

            // Special handling for individual_prep - generate all prep documents
            if (docType === 'individual_prep') {
                const response = await FluxGen.api.post('/documents/generate-all-prep');
                FluxGen.ui.showFlashMessage(`Generated ${response.total_generated} prep documents successfully`, 'success');
            } else {
                const response = await FluxGen.api.post(`/documents/generate/${docType}`);
                FluxGen.ui.showFlashMessage(response.message, 'success');
            }

            // Reload files list
            await this.loadGeneratedFiles();

        } catch (error) {
            console.error(`Error generating ${docType}:`, error);
            FluxGen.ui.showFlashMessage(`Error generating document: ${error.message}`, 'error');

            statusEl.textContent = 'Generation failed';
            statusEl.className = 'text-xs text-red-600';
        } finally {
            FluxGen.ui.showLoading(generateBtn, false);
        }
    }

    async generateAllDocuments() {
        this.showProgressModal();
        
        try {
            let completedCount = 0;
            const totalCount = this.documents.length;
            
            // Update progress
            this.updateProgress(completedCount, totalCount, 'Starting document generation...');
            
            const response = await FluxGen.api.post('/documents/generate-all');
            
            // Simulate progress updates (in real implementation, this would come from server events)
            for (let i = 0; i < totalCount; i++) {
                await new Promise(resolve => setTimeout(resolve, 500)); // Simulate processing time
                completedCount++;
                const docTitle = this.getDocumentTitle(this.documents[i]);
                this.updateProgress(completedCount, totalCount, `Generated ${docTitle}`);
            }
            
            // Show results
            this.showGenerationResults(response);
            
            // Reload files list
            await this.loadGeneratedFiles();
            
        } catch (error) {
            console.error('Error generating all documents:', error);
            FluxGen.ui.showFlashMessage(`Error generating documents: ${error.message}`, 'error');
            this.hideProgressModal();
        }
    }

    showProgressModal() {
        const modal = document.getElementById('progress-modal');
        const closeBtn = document.getElementById('progress-close');
        
        modal.classList.remove('hidden');
        closeBtn.classList.add('hidden');
        
        // Reset progress
        this.updateProgress(0, this.documents.length, 'Initializing...');
        
        // Hide results
        const resultsDiv = document.getElementById('generation-results');
        resultsDiv.classList.add('hidden');
        resultsDiv.innerHTML = '';
    }

    hideProgressModal() {
        const modal = document.getElementById('progress-modal');
        modal.classList.add('hidden');
    }

    updateProgress(completed, total, message) {
        const progressBar = document.getElementById('progress-bar');
        const progressCounter = document.getElementById('progress-counter');
        const currentDocument = document.getElementById('current-document');
        
        const percentage = (completed / total) * 100;
        
        progressBar.style.width = `${percentage}%`;
        progressCounter.textContent = `${completed} / ${total}`;
        currentDocument.textContent = message;
    }

    showGenerationResults(response) {
        const resultsDiv = document.getElementById('generation-results');
        const closeBtn = document.getElementById('progress-close');
        
        // Show results
        const successCount = response.total_generated || 0;
        const errorCount = response.total_errors || 0;
        
        let resultsHTML = `
            <div class="text-sm">
                <div class="font-medium text-gray-900 mb-2">Generation Complete</div>
                <div class="text-green-600">✓ ${successCount} documents generated successfully</div>
        `;
        
        if (errorCount > 0) {
            resultsHTML += `<div class="text-red-600">✗ ${errorCount} documents failed</div>`;
        }
        
        resultsHTML += '</div>';
        
        resultsDiv.innerHTML = resultsHTML;
        resultsDiv.classList.remove('hidden');
        
        // Show close button
        closeBtn.classList.remove('hidden');
        
        // Show flash message
        if (errorCount === 0) {
            FluxGen.ui.showFlashMessage('All documents generated successfully!', 'success');
        } else {
            FluxGen.ui.showFlashMessage(`Generated ${successCount} documents with ${errorCount} errors`, 'warning');
        }
    }

    downloadDocument(docType) {
        const card = document.querySelector(`[data-doc="${docType}"]`);
        const downloadBtn = card.querySelector('.download-btn');
        const filename = downloadBtn.dataset.filename;
        
        if (filename) {
            this.downloadFile(filename);
        } else {
            FluxGen.ui.showFlashMessage('No file available for download', 'warning');
        }
    }

    downloadFile(filename) {
        const downloadUrl = `/api/documents/download/${filename}`;
        
        // Create temporary link and trigger download
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.download = filename;
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
        
        FluxGen.ui.showFlashMessage('Download started', 'info', 2000);
    }

    async deleteFile(filename) {
        if (!confirm(`Are you sure you want to delete ${filename}?`)) {
            return;
        }

        try {
            await FluxGen.api.delete(`/documents/${filename}`);
            FluxGen.ui.showFlashMessage('File deleted successfully', 'success');
            
            // Reload files list
            await this.loadGeneratedFiles();
            
        } catch (error) {
            console.error('Error deleting file:', error);
            FluxGen.ui.showFlashMessage('Error deleting file', 'error');
        }
    }

    // Utility methods
    extractDocType(filename) {
        // Special case mappings for filenames that don't match doc type exactly
        const specialMappings = {
            'team_biographies': 'team_bios',
            'prep_': 'individual_prep'
        };

        // Check special mappings first
        for (const [filenamePattern, docType] of Object.entries(specialMappings)) {
            if (filename.includes(filenamePattern)) {
                return docType;
            }
        }

        // Then check standard doc types
        for (const docType of this.documents) {
            if (filename.includes(docType)) {
                return docType;
            }
        }

        return 'unknown';
    }

    getDocumentTitle(docType) {
        const titles = {
            'executive_summary': 'Executive Summary',
            'business_plan': 'Business Plan',
            'financial_projections': 'Financial Projections',
            'market_analysis': 'Market Analysis',
            'technical_specs': 'Technical Specifications',
            'team_bios': 'Team Biographies',
            'site_requirements': 'Site Requirements',
            'pitch_deck': 'Pitch Deck',
            'individual_prep': 'Individual Prep Document'
        };

        return titles[docType] || 'Unknown Document';
    }
}

// Initialize document manager when DOM is loaded
let documentManager;

document.addEventListener('DOMContentLoaded', function() {
    documentManager = new DocumentManager();
    
    // Make it globally available for onclick handlers
    window.documentManager = documentManager;
});
