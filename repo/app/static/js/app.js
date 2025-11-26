// FluxGen Industries - Main JavaScript Application

// Global utilities and common functions
const FluxGen = {
    // API base URL
    apiBase: '/api',
    
    // Common UI utilities
    ui: {
        showFlashMessage: function(message, type = 'info', duration = 5000) {
            const container = document.getElementById('flash-messages');
            if (!container) return;
            
            const messageEl = document.createElement('div');
            messageEl.className = `flash-message ${type}`;
            messageEl.innerHTML = `
                <div class="flex justify-between items-center">
                    <span>${message}</span>
                    <button onclick="this.parentElement.parentElement.remove()" class="ml-4 text-lg leading-none">&times;</button>
                </div>
            `;
            
            container.appendChild(messageEl);
            
            // Auto remove after duration
            setTimeout(() => {
                if (messageEl.parentElement) {
                    messageEl.remove();
                }
            }, duration);
        },
        
        showLoading: function(element, show = true) {
            if (show) {
                element.classList.add('loading');
            } else {
                element.classList.remove('loading');
            }
        },
        
        formatCurrency: function(amount, currency = 'CAD') {
            return new Intl.NumberFormat('en-CA', {
                style: 'currency',
                currency: currency
            }).format(amount || 0);
        },
        
        formatDate: function(dateString) {
            if (!dateString) return 'N/A';
            try {
                const date = new Date(dateString);
                return date.toLocaleDateString('en-CA', {
                    year: 'numeric',
                    month: 'long',
                    day: 'numeric'
                });
            } catch (error) {
                return dateString;
            }
        },
        
        formatDateTime: function(dateString) {
            if (!dateString) return 'N/A';
            try {
                const date = new Date(dateString);
                return date.toLocaleString('en-CA', {
                    year: 'numeric',
                    month: 'short',
                    day: 'numeric',
                    hour: '2-digit',
                    minute: '2-digit'
                });
            } catch (error) {
                return dateString;
            }
        },
        
        formatFileSize: function(bytes) {
            if (bytes === 0) return '0 Bytes';
            const k = 1024;
            const sizes = ['Bytes', 'KB', 'MB', 'GB'];
            const i = Math.floor(Math.log(bytes) / Math.log(k));
            return parseFloat((bytes / Math.pow(k, i)).toFixed(2)) + ' ' + sizes[i];
        },
        
        debounce: function(func, delay) {
            let timeoutId;
            return function (...args) {
                clearTimeout(timeoutId);
                timeoutId = setTimeout(() => func.apply(this, args), delay);
            };
        }
    },
    
    // API utilities
    api: {
        request: async function(endpoint, options = {}) {
            const url = `${FluxGen.apiBase}${endpoint}`;
            const defaultOptions = {
                headers: {
                    'Content-Type': 'application/json',
                },
            };
            
            const finalOptions = { ...defaultOptions, ...options };
            
            try {
                const response = await fetch(url, finalOptions);
                const data = await response.json();
                
                if (!response.ok) {
                    throw new Error(data.error || `HTTP error! status: ${response.status}`);
                }
                
                return data;
            } catch (error) {
                console.error('API request failed:', error);
                throw error;
            }
        },
        
        get: function(endpoint) {
            return this.request(endpoint);
        },
        
        post: function(endpoint, data) {
            return this.request(endpoint, {
                method: 'POST',
                body: JSON.stringify(data)
            });
        },
        
        put: function(endpoint, data) {
            return this.request(endpoint, {
                method: 'PUT',
                body: JSON.stringify(data)
            });
        },
        
        delete: function(endpoint) {
            return this.request(endpoint, {
                method: 'DELETE'
            });
        }
    },
    
    // Form utilities
    forms: {
        serialize: function(form) {
            const formData = new FormData(form);
            const data = {};
            for (const [key, value] of formData.entries()) {
                data[key] = value;
            }
            return data;
        },
        
        populate: function(form, data) {
            Object.keys(data).forEach(key => {
                const field = form.querySelector(`[name="${key}"]`);
                if (field) {
                    field.value = data[key] || '';
                }
            });
        },
        
        reset: function(form) {
            form.reset();
            // Clear any custom validation states
            const inputs = form.querySelectorAll('input, textarea, select');
            inputs.forEach(input => {
                input.classList.remove('border-red-500', 'border-green-500');
            });
        },
        
        validate: function(form) {
            const inputs = form.querySelectorAll('input[required], textarea[required], select[required]');
            let isValid = true;
            
            inputs.forEach(input => {
                if (!input.value.trim()) {
                    input.classList.add('border-red-500');
                    input.classList.remove('border-green-500');
                    isValid = false;
                } else {
                    input.classList.remove('border-red-500');
                    input.classList.add('border-green-500');
                }
            });
            
            return isValid;
        }
    },
    
    // Table utilities
    tables: {
        createRow: function(data, columns, actions = []) {
            const row = document.createElement('tr');
            row.className = 'table-row';
            
            // Add data columns
            columns.forEach(column => {
                const cell = document.createElement('td');
                cell.className = 'px-6 py-4 whitespace-nowrap text-sm text-gray-900';
                
                let value = data[column.key];
                if (column.format) {
                    value = column.format(value, data);
                } else if (column.key === 'created_date') {
                    value = FluxGen.ui.formatDateTime(value);
                }

                const displayValue = value || 'N/A';
                if (column.asHtml) {
                    cell.innerHTML = displayValue;
                } else {
                    cell.textContent = displayValue;
                }
                row.appendChild(cell);
            });
            
            // Add actions column
            if (actions.length > 0) {
                const actionsCell = document.createElement('td');
                actionsCell.className = 'px-6 py-4 whitespace-nowrap text-sm font-medium';
                
                const actionsDiv = document.createElement('div');
                actionsDiv.className = 'flex space-x-2';
                
                actions.forEach(action => {
                    const button = document.createElement('button');
                    button.className = action.class || 'text-fluxgen-orange hover:text-fluxgen-navy';
                    button.textContent = action.text;
                    button.addEventListener('click', () => action.handler(data));
                    actionsDiv.appendChild(button);
                });
                
                actionsCell.appendChild(actionsDiv);
                row.appendChild(actionsCell);
            }
            
            return row;
        },
        
        updateTable: function(tableBodyId, data, columns, actions = []) {
            const tbody = document.getElementById(tableBodyId);
            if (!tbody) return;
            
            // Clear existing rows
            tbody.innerHTML = '';
            
            if (data.length === 0) {
                const emptyRow = document.createElement('tr');
                const emptyCell = document.createElement('td');
                emptyCell.colSpan = columns.length + (actions.length > 0 ? 1 : 0);
                emptyCell.className = 'px-6 py-8 text-center text-gray-500';
                emptyCell.textContent = 'No data available';
                emptyRow.appendChild(emptyCell);
                tbody.appendChild(emptyRow);
                return;
            }
            
            // Add data rows
            data.forEach(item => {
                const row = this.createRow(item, columns, actions);
                tbody.appendChild(row);
            });
        }
    }
};

// Global function for flash messages (backward compatibility)
function showFlashMessage(message, type, duration) {
    FluxGen.ui.showFlashMessage(message, type, duration);
}

// Mobile menu functionality
document.addEventListener('DOMContentLoaded', function() {
    const mobileMenuButton = document.getElementById('mobile-menu-button');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function() {
            mobileMenu.classList.toggle('hidden');
        });
        
        // Close mobile menu when clicking outside
        document.addEventListener('click', function(event) {
            if (!mobileMenuButton.contains(event.target) && !mobileMenu.contains(event.target)) {
                mobileMenu.classList.add('hidden');
            }
        });
    }
    
    // Add smooth scrolling to anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Add keyboard navigation support
    document.addEventListener('keydown', function(event) {
        if (event.key === 'Escape') {
            // Close any open modals
            const modals = document.querySelectorAll('.modal, [id$="-modal"]');
            modals.forEach(modal => {
                if (!modal.classList.contains('hidden')) {
                    modal.classList.add('hidden');
                }
            });
        }
    });
    
    // Add loading states to form submissions
    document.addEventListener('submit', function(event) {
        const form = event.target;
        if (form.tagName === 'FORM') {
            const submitButton = form.querySelector('button[type="submit"]');
            if (submitButton) {
                FluxGen.ui.showLoading(submitButton, true);
                
                // Reset loading state after a delay (fallback)
                setTimeout(() => {
                    FluxGen.ui.showLoading(submitButton, false);
                }, 10000);
            }
        }
    });
    
    // Add auto-save functionality for forms with data-autosave attribute
    document.querySelectorAll('form[data-autosave]').forEach(form => {
        const inputs = form.querySelectorAll('input, textarea, select');
        const saveDelay = parseInt(form.dataset.autosave) || 2000;
        
        const autoSave = FluxGen.ui.debounce(async function() {
            try {
                const data = FluxGen.forms.serialize(form);
                const endpoint = form.dataset.endpoint || form.action;
                
                if (endpoint) {
                    await FluxGen.api.put(endpoint, data);
                    FluxGen.ui.showFlashMessage('Changes saved automatically', 'info', 2000);
                }
            } catch (error) {
                console.error('Auto-save failed:', error);
            }
        }, saveDelay);
        
        inputs.forEach(input => {
            input.addEventListener('input', autoSave);
        });
    });
});

// Error handling for unhandled promise rejections
window.addEventListener('unhandledrejection', function(event) {
    console.error('Unhandled promise rejection:', event.reason);
    FluxGen.ui.showFlashMessage('An unexpected error occurred. Please try again.', 'error');
    event.preventDefault();
});

// Service worker registration for offline functionality (future enhancement)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        // Service worker registration can be added here for offline capabilities
    });
}

// Export for module usage
if (typeof module !== 'undefined' && module.exports) {
    module.exports = FluxGen;
}

// Make FluxGen globally available
window.FluxGen = FluxGen;
