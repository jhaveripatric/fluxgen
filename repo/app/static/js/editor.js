// FluxGen Data Editor JavaScript

class DataEditor {
    constructor() {
        this.currentTab = 'company';
        this.data = {};
        this.init();
    }

    init() {
        this.setupTabs();
        this.setupEventHandlers();
        this.loadAllData();
    }

    setupTabs() {
        const tabButtons = document.querySelectorAll('.tab-button');
        const tabContents = document.querySelectorAll('.tab-content');

        tabButtons.forEach(button => {
            button.addEventListener('click', () => {
                const tabName = button.dataset.tab;
                this.switchTab(tabName);
            });
        });

        // Initialize first tab
        this.switchTab('company');
    }

    switchTab(tabName) {
        // Update button states
        document.querySelectorAll('.tab-button').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');

        // Update content visibility
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.add('hidden');
        });
        document.getElementById(`tab-${tabName}`).classList.remove('hidden');

        this.currentTab = tabName;
        this.loadTabData(tabName);
    }

    setupEventHandlers() {
        // Company form
        const companyForm = document.getElementById('company-form');
        if (companyForm) {
            companyForm.addEventListener('submit', (e) => this.handleCompanySubmit(e));
        }

        // Team member modal
        const addTeamBtn = document.getElementById('add-team-member');
        const teamModal = document.getElementById('team-modal');
        const teamForm = document.getElementById('team-form');
        const modalCancel = document.getElementById('team-modal-cancel');

        if (addTeamBtn) {
            addTeamBtn.addEventListener('click', () => this.showTeamModal());
        }

        if (modalCancel) {
            modalCancel.addEventListener('click', () => this.hideTeamModal());
        }

        if (teamForm) {
            teamForm.addEventListener('submit', (e) => this.handleTeamSubmit(e));
        }

        // Close modal on outside click
        if (teamModal) {
            teamModal.addEventListener('click', (e) => {
                if (e.target === teamModal) {
                    this.hideTeamModal();
                }
            });
        }
    }

    async loadAllData() {
        try {
            // Load company data
            const companyData = await FluxGen.api.get('/data/company');
            this.data.company = companyData;

            // Load team data
            const teamData = await FluxGen.api.get('/data/team');
            this.data.team = teamData;

            // Load other data
            const [
                capexData,
                productionData,
                alloysData,
                fundingData,
                certificationsData,
                assumptionsData,
                marketData,
                competitorsData,
                pricingData,
                materialsData
            ] = await Promise.all([
                FluxGen.api.get('/data/capex'),
                FluxGen.api.get('/data/production'),
                FluxGen.api.get('/data/alloys'),
                FluxGen.api.get('/data/funding'),
                FluxGen.api.get('/data/certifications'),
                FluxGen.api.get('/data/assumptions'),
                FluxGen.api.get('/data/market-analysis'),
                FluxGen.api.get('/data/competitors'),
                FluxGen.api.get('/data/competitor-pricing'),
                FluxGen.api.get('/data/raw-materials')
            ]);

            this.data.capex = capexData;
            this.data.production = productionData;
            this.data.alloys = alloysData;
            this.data.funding = fundingData;
            this.data.certifications = certificationsData;
            this.data.assumptions = assumptionsData;
            this.data.market = marketData;
            this.data.competitors = competitorsData;
            this.data.pricing = pricingData;
            this.data.materials = materialsData;

            // Populate current tab
            this.loadTabData(this.currentTab);

        } catch (error) {
            console.error('Error loading data:', error);
            FluxGen.ui.showFlashMessage('Error loading data', 'error');
        }
    }

    loadTabData(tabName) {
        switch (tabName) {
            case 'company':
                this.loadCompanyData();
                break;
            case 'team':
                this.loadTeamData();
                break;
            case 'capex':
                this.loadCapexData();
                break;
            case 'production':
                this.loadProductionData();
                break;
            case 'alloys':
                this.loadAlloysData();
                break;
            case 'funding':
                this.loadFundingData();
                break;
            case 'certifications':
                this.loadCertificationsData();
                break;
            case 'assumptions':
                this.loadAssumptionsData();
                break;
            case 'market':
                this.loadMarketData();
                break;
            case 'competitors':
                this.loadCompetitorsData();
                break;
            case 'pricing':
                this.loadPricingData();
                break;
            case 'materials':
                this.loadMaterialsData();
                break;
        }
    }

    loadCompanyData() {
        const form = document.getElementById('company-form');
        if (form && this.data.company) {
            FluxGen.forms.populate(form, this.data.company);
        }
    }

    loadTeamData() {
        const columns = [
            { key: 'name', format: null },
            { key: 'role', format: null },
            { key: 'email', format: (value) => value || 'N/A' },
            { key: 'phone', format: (value) => value || 'N/A' },
            { key: 'status', format: (value) => this.formatStatus(value), asHtml: true }
        ];

        const actions = [
            {
                text: 'Edit',
                class: 'text-fluxgen-orange hover:text-fluxgen-navy mr-2',
                handler: (data) => this.editTeamMember(data)
            },
            {
                text: 'Delete',
                class: 'text-red-600 hover:text-red-800',
                handler: (data) => this.deleteTeamMember(data)
            }
        ];

        FluxGen.tables.updateTable('team-table-body', this.data.team || [], columns, actions);
    }

    loadCapexData() {
        const columns = [
            { key: 'category', format: null },
            { key: 'description', format: (value) => this.truncateText(value, 50) },
            { key: 'estimated_cost_cad', format: (value) => FluxGen.ui.formatCurrency(value) },
            { key: 'phase', format: null },
            { key: 'status', format: (value) => this.formatStatus(value), asHtml: true }
        ];

        const actions = [
            {
                text: 'Edit',
                class: 'text-fluxgen-orange hover:text-fluxgen-navy',
                handler: (data) => this.editCapexItem(data)
            }
        ];

        FluxGen.tables.updateTable('capex-table-body', this.data.capex || [], columns, actions);
    }

    loadProductionData() {
        const columns = [
            { key: 'phase', format: null },
            { key: 'output_kg_month', format: (value) => value ? `${value.toLocaleString()} kg` : 'N/A' },
            { key: 'facility_type', format: null },
            { key: 'process_flow', format: (value) => this.truncateText(value, 40) },
            { key: 'sourcing_strategy', format: (value) => this.truncateText(value, 30) }
        ];

        const actions = [
            {
                text: 'Edit',
                class: 'text-fluxgen-orange hover:text-fluxgen-navy',
                handler: (data) => this.editProductionTarget(data)
            }
        ];

        FluxGen.tables.updateTable('production-table-body', this.data.production || [], columns, actions);
    }

    loadAlloysData() {
        const columns = [
            { key: 'alloy_symbol', format: null },
            { key: 'alloy_name', format: (value) => this.truncateText(value, 25) },
            { key: 'grade_type', format: null },
            { key: 'application', format: (value) => this.truncateText(value, 40) },
            { key: 'unit_cost_cad', format: (value) => FluxGen.ui.formatCurrency(value) }
        ];

        FluxGen.tables.updateTable('alloys-table-body', this.data.alloys || [], columns);
    }

    loadFundingData() {
        const columns = [
            { key: 'program_name', format: (value) => this.truncateText(value, 30) },
            { key: 'funding_type', format: null },
            { key: 'max_coverage_percent', format: (value) => value ? `${value}%` : 'N/A' },
            { key: 'max_amount_cad', format: (value) => FluxGen.ui.formatCurrency(value) },
            { key: 'application_status', format: (value) => this.formatStatus(value) }
        ];

        FluxGen.tables.updateTable('funding-table-body', this.data.funding || [], columns);
    }

    loadCertificationsData() {
        const columns = [
            { key: 'phase', format: (value) => `Phase ${value}` },
            { key: 'certification_name', format: (value) => this.truncateText(value, 30) },
            { key: 'certification_body', format: null },
            { key: 'target_date', format: (value) => FluxGen.ui.formatDate(value) },
            { key: 'status', format: (value) => this.formatStatus(value), asHtml: true },
            { key: 'cost_estimate_cad', format: (value) => FluxGen.ui.formatCurrency(value) }
        ];

        FluxGen.tables.updateTable('certifications-table-body', this.data.certifications || [], columns);
    }

    loadAssumptionsData() {
        const columns = [
            { key: 'phase', format: null },
            { key: 'category', format: null },
            { key: 'assumption_name', format: (value) => this.truncateText(value, 40) },
            { key: 'value_numeric', format: (value, row) => this.formatValue(value, row.value_text, row.unit) },
            { key: 'unit', format: null },
            { key: 'confidence_level', format: (value) => value || 'N/A' }
        ];

        FluxGen.tables.updateTable('assumptions-table-body', this.data.assumptions || [], columns);
    }

    loadMarketData() {
        const columns = [
            { key: 'category', format: null },
            { key: 'metric', format: (value) => this.truncateText(value, 40) },
            { key: 'value_numeric', format: (value, row) => this.formatValue(value, row.value_text, row.unit) },
            { key: 'year', format: (value) => value || '—' },
            { key: 'source', format: (value) => this.truncateText(value, 30) }
        ];

        FluxGen.tables.updateTable('market-table-body', this.data.market || [], columns);
    }

    loadCompetitorsData() {
        const columns = [
            { key: 'company_name', format: null },
            { key: 'website', format: (value) => value ? `<a class="text-fluxgen-orange hover:underline" href=\"${value}\" target=\"_blank\" rel=\"noopener\">Link</a>` : 'N/A', asHtml: true },
            { key: 'contact_info', format: (value) => value || 'N/A' },
            { key: 'notes', format: (value) => this.truncateText(value, 60) }
        ];

        FluxGen.tables.updateTable('competitors-table-body', this.data.competitors || [], columns);
    }

    loadPricingData() {
        const columns = [
            { key: 'flux_name', format: null },
            { key: 'price_usd', format: (value) => value ? `$${value}` : 'N/A' },
            { key: 'unit_pounds', format: (value) => value ? `${value} lbs` : 'N/A' },
            { key: 'price_per_pound', format: (value) => value ? `$${value}` : 'N/A' },
            { key: 'supplier', format: null }
        ];

        FluxGen.tables.updateTable('pricing-table-body', this.data.pricing || [], columns);
    }

    loadMaterialsData() {
        const columns = [
            { key: 'material_name', format: null },
            { key: 'batch_mark', format: (value) => value || 'N/A' },
            { key: 'sio2', format: (value) => this.formatPercent(value) },
            { key: 'caco3', format: (value) => this.formatPercent(value) },
            { key: 'fe2o3', format: (value) => this.formatPercent(value) },
            { key: 'notes', format: (value) => this.truncateText(value, 40) }
        ];

        FluxGen.tables.updateTable('materials-table-body', this.data.materials || [], columns);
    }

    async handleCompanySubmit(e) {
        e.preventDefault();
        
        const form = e.target;
        const submitButton = form.querySelector('button[type="submit"]');
        
        try {
            FluxGen.ui.showLoading(submitButton, true);
            
            const data = FluxGen.forms.serialize(form);
            await FluxGen.api.put('/data/company', data);
            
            this.data.company = { ...this.data.company, ...data };
            FluxGen.ui.showFlashMessage('Company information updated successfully', 'success');
            
        } catch (error) {
            console.error('Error updating company:', error);
            FluxGen.ui.showFlashMessage('Error updating company information', 'error');
        } finally {
            FluxGen.ui.showLoading(submitButton, false);
        }
    }

    showTeamModal(member = null) {
        const modal = document.getElementById('team-modal');
        const form = document.getElementById('team-form');
        const title = document.getElementById('team-modal-title');

        if (member) {
            title.textContent = 'Edit Team Member';
            FluxGen.forms.populate(form, member);
        } else {
            title.textContent = 'Add Team Member';
            FluxGen.forms.reset(form);
        }

        modal.classList.remove('hidden');
    }

    hideTeamModal() {
        const modal = document.getElementById('team-modal');
        modal.classList.add('hidden');
    }

    async handleTeamSubmit(e) {
        e.preventDefault();
        
        const form = e.target;
        const submitButton = form.querySelector('button[type="submit"]');
        
        try {
            FluxGen.ui.showLoading(submitButton, true);
            
            const data = FluxGen.forms.serialize(form);
            const memberId = data.id;
            
            if (memberId) {
                // Update existing member
                await FluxGen.api.put(`/data/team/${memberId}`, data);
                FluxGen.ui.showFlashMessage('Team member updated successfully', 'success');
            } else {
                // Add new member
                await FluxGen.api.post('/data/team', data);
                FluxGen.ui.showFlashMessage('Team member added successfully', 'success');
            }
            
            // Reload team data
            this.data.team = await FluxGen.api.get('/data/team');
            this.loadTeamData();
            this.hideTeamModal();
            
        } catch (error) {
            console.error('Error saving team member:', error);
            FluxGen.ui.showFlashMessage('Error saving team member', 'error');
        } finally {
            FluxGen.ui.showLoading(submitButton, false);
        }
    }

    editTeamMember(member) {
        this.showTeamModal(member);
    }

    async deleteTeamMember(member) {
        if (!confirm(`Are you sure you want to delete ${member.name}?`)) {
            return;
        }

        try {
            await FluxGen.api.delete(`/data/team/${member.id}`);
            this.data.team = this.data.team.filter(m => m.id !== member.id);
            this.loadTeamData();
            FluxGen.ui.showFlashMessage('Team member deleted successfully', 'success');
        } catch (error) {
            console.error('Error deleting team member:', error);
            FluxGen.ui.showFlashMessage('Error deleting team member', 'error');
        }
    }

    editCapexItem(item) {
        // Simple inline editing for CAPEX items
        const newValue = prompt(`Edit estimated cost for ${item.category}:`, item.estimated_cost_cad);
        
        if (newValue !== null && !isNaN(newValue)) {
            this.updateCapexItem(item.id, { estimated_cost_cad: parseFloat(newValue) });
        }
    }

    async updateCapexItem(id, data) {
        try {
            await FluxGen.api.put(`/data/capex/${id}`, data);
            
            // Update local data
            const index = this.data.capex.findIndex(item => item.id === id);
            if (index !== -1) {
                this.data.capex[index] = { ...this.data.capex[index], ...data };
                this.loadCapexData();
            }
            
            FluxGen.ui.showFlashMessage('CAPEX item updated successfully', 'success');
        } catch (error) {
            console.error('Error updating CAPEX item:', error);
            FluxGen.ui.showFlashMessage('Error updating CAPEX item', 'error');
        }
    }

    editProductionTarget(target) {
        // Simple inline editing for production targets
        const newValue = prompt(`Edit output (kg/month) for ${target.phase} phase:`, target.output_kg_month);
        
        if (newValue !== null && !isNaN(newValue)) {
            this.updateProductionTarget(target.id, { output_kg_month: parseInt(newValue) });
        }
    }

    async updateProductionTarget(id, data) {
        try {
            await FluxGen.api.put(`/data/production/${id}`, data);
            
            // Update local data
            const index = this.data.production.findIndex(item => item.id === id);
            if (index !== -1) {
                this.data.production[index] = { ...this.data.production[index], ...data };
                this.loadProductionData();
            }
            
            FluxGen.ui.showFlashMessage('Production target updated successfully', 'success');
        } catch (error) {
            console.error('Error updating production target:', error);
            FluxGen.ui.showFlashMessage('Error updating production target', 'error');
        }
    }

    // Utility methods
    formatStatus(status) {
        const statusClass = {
            'active': 'status-active',
            'inactive': 'status-inactive',
            'pending': 'status-pending',
            'completed': 'status-completed',
            'planned': 'status-pending',
            'identified': 'status-pending'
        };

        const className = statusClass[status?.toLowerCase()] || 'status-pending';
        return `<span class="status-badge ${className}">${status || 'N/A'}</span>`;
    }

    truncateText(text, maxLength) {
        if (!text) return 'N/A';
        return text.length > maxLength ? text.substring(0, maxLength) + '...' : text;
    }

    formatValue(numeric, textValue, unit) {
        if (numeric !== null && numeric !== undefined) {
            return unit ? `${numeric} ${unit}` : numeric;
        }
        if (textValue) return textValue;
        return 'N/A';
    }

    formatPercent(value) {
        if (value === null || value === undefined) return 'N/A';
        return `${value}%`;
    }
}

// Initialize editor when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new DataEditor();
});
