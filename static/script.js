// Oracle 120 Quẻ - TECH ORACLE 2026 - Đại Pháp Sư Thùy Linh
class OracleApp {
    constructor() {
        this.currentOracle = null;
        this.isLoading = false;
        this.typewriterSpeed = 15; // Tăng tốc độ lên 15ms cho hiệu ứng nhanh
        this.init();
    }

    init() {
        this.bindEvents();
        this.setupAnimations();
        console.log('🔮 TECH ORACLE 2026 - Đại Pháp Sư Thùy Linh initialized');
    }

    bindEvents() {
        // Oracle button clicks
        document.querySelectorAll('.oracle-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                const category = btn.dataset.category;
                const color = btn.dataset.color;
                this.requestOracle(category, color);
            });
        });

        // Form inputs
        document.getElementById('userName').addEventListener('input', () => this.validateForm());
        document.getElementById('userBirthday').addEventListener('change', () => this.validateForm());
        document.getElementById('userZodiac').addEventListener('change', () => this.validateForm());
    }

    setupAnimations() {
        // Add floating animation to crystal ball on load
        const crystalBall = document.getElementById('crystalBall');
        if (crystalBall) {
            crystalBall.style.animation = 'float 6s ease-in-out infinite';
        }
    }

    validateForm() {
        const name = document.getElementById('userName').value.trim();
        const birthday = document.getElementById('userBirthday').value;
        const zodiac = document.getElementById('userZodiac').value;
        
        return name && birthday && zodiac;
    }

    async requestOracle(category, color) {
        if (this.isLoading) return;

        // Validate user information
        if (!this.validateForm()) {
            this.showNotification('Vui lòng điền đầy đủ thông tin trước khi xem quẻ!', 'warning');
            this.highlightFormFields();
            return;
        }

        this.isLoading = true;
        this.showLoading();
        this.animateCrystalBall(color);

        try {
            // Get user information
            const userData = this.getUserData();
            
            // Make API request
            const response = await fetch(`/api/oracle/${category}?${new URLSearchParams(userData)}`);
            const data = await response.json();

            if (data.success) {
                this.currentOracle = data;
                this.displayOracle(data, category, color);
                this.hideLoading();
            } else {
                throw new Error(data.message || 'Có lỗi xảy ra');
            }
        } catch (error) {
            console.error('Oracle request error:', error);
            this.showNotification('Không thể kết nối với vũ trụ. Vui lòng thử lại!', 'error');
            this.hideLoading();
        } finally {
            this.isLoading = false;
            this.resetCrystalBall();
        }
    }

    getUserData() {
        return {
            name: document.getElementById('userName').value.trim(),
            birthday: document.getElementById('userBirthday').value,
            zodiac: document.getElementById('userZodiac').value
        };
    }

    highlightFormFields() {
        const fields = ['userName', 'userBirthday', 'userZodiac'];
        fields.forEach(fieldId => {
            const field = document.getElementById(fieldId);
            if (!field.value.trim()) {
                field.style.borderColor = '#EF4444';
                field.style.boxShadow = '0 0 0 3px rgba(239, 68, 68, 0.1)';
                
                setTimeout(() => {
                    field.style.borderColor = '';
                    field.style.boxShadow = '';
                }, 3000);
            }
        });
    }

    animateCrystalBall(color) {
        const crystalBall = document.getElementById('crystalBall');
        const crystalStatus = document.getElementById('crystalStatus');
        
        // Remove all color classes
        crystalBall.classList.remove('gold', 'pink', 'cyan', 'purple', 'green', 'orange');
        
        // Add appropriate color class based on category
        const colorMap = {
            '#FF1493': 'pink',
            '#00CED1': 'cyan', 
            '#00FF00': 'green',
            '#FFD700': 'gold',
            '#FF8C00': 'orange',
            '#9370DB': 'purple'
        };
        
        const colorClass = colorMap[color] || 'gold';
        crystalBall.classList.add(colorClass);
        
        // Update status
        crystalStatus.textContent = '🔮 Quả cầu pha lê đang kết nối với vũ trụ...';
        crystalStatus.style.animation = 'pulse 1s ease-in-out infinite';
    }

    resetCrystalBall() {
        const crystalBall = document.getElementById('crystalBall');
        const crystalStatus = document.getElementById('crystalStatus');
        
        // Remove color classes
        crystalBall.classList.remove('gold', 'pink', 'cyan', 'purple', 'green', 'orange');
        
        // Reset status
        crystalStatus.textContent = '🔮 Quả cầu pha lê đang chờ...';
        crystalStatus.style.animation = '';
    }

    displayOracle(oracleData, category, color) {
        const resultSection = document.getElementById('oracleResult');
        const resultCategory = document.getElementById('resultCategory');
        const resultTime = document.getElementById('resultTime');
        const oracleText = document.getElementById('oracleText');
        const thuyLinhText = document.getElementById('thuyLinhText');
        const resultName = document.getElementById('resultName');
        const resultBirthday = document.getElementById('resultBirthday');
        const resultZodiac = document.getElementById('resultZodiac');

        // Set category title
        const categoryNames = {
            'vận_may': 'THẺ BÀI VẬN MAY',
            'tình_duyên': 'THẺ BÀI TÌNH DUYÊN',
            'sự_nghiệp': 'THẺ BÀI SỰ NGHIỆP',
            'tiền_tài': 'THẺ BÀI TIỀN TÀI',
            'sức_khỏe': 'THẺ BÀI SỨC KHỎE',
            'vũ_trụ': 'THẺ BÀI VŨ TRỤ GỬI THÔNG ĐIỆP'
        };
        
        resultCategory.textContent = categoryNames[category] || 'THẺ BÀI ĐỊNH MỆNH';
        resultTime.textContent = `Thời gian: ${new Date(oracleData.timestamp).toLocaleString('vi-VN')}`;
        
        // Set user information
        const userData = this.getUserData();
        resultName.textContent = userData.name;
        resultBirthday.textContent = userData.birthday;
        resultZodiac.textContent = userData.zodiac;

        // Show result section with animation
        resultSection.style.display = 'block';
        resultSection.scrollIntoView({ behavior: 'smooth', block: 'center' });

        // Add special effects
        this.addDestinyCardEffects(color);
        
        // Apply typewriter effect to oracle text
        this.typewriterEffect(oracleText, oracleData.oracle);
        
        // Apply typewriter effect to Thùy Linh message
        this.typewriterEffect(thuyLinhText, oracleData.thuy_linh_message, 30);
        
        // Show success notification
        this.showNotification('Quẻ của bạn đã sẵn sàng!', 'success');
    }

    typewriterEffect(element, text, speed = null) {
        const typingSpeed = speed || this.typewriterSpeed;
        element.textContent = '';
        element.style.opacity = '1';
        
        let i = 0;
        const type = () => {
            if (i < text.length) {
                element.textContent += text.charAt(i);
                i++;
                setTimeout(type, typingSpeed);
            }
        };
        
        type();
    }

    addDestinyCardEffects(color) {
        const destinyCard = document.querySelector('.destiny-card');
        if (destinyCard) {
            // Add glow effect based on category color
            destinyCard.style.boxShadow = `0 0 50px ${color}40, 0 20px 25px -5px rgba(0, 0, 0, 0.1)`;
            
            // Remove effect after 3 seconds
            setTimeout(() => {
                destinyCard.style.boxShadow = '';
            }, 3000);
        }
    }

    showLoading() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        loadingOverlay.style.display = 'flex';
    }

    hideLoading() {
        const loadingOverlay = document.getElementById('loadingOverlay');
        loadingOverlay.style.display = 'none';
    }

    showNotification(message, type = 'info') {
        const notification = document.getElementById('notification');
        
        // Remove existing classes
        notification.classList.remove('success', 'error', 'warning');
        
        // Add new class
        notification.classList.add(type);
        notification.textContent = message;
        notification.style.display = 'block';

        // Auto hide after 3 seconds
        setTimeout(() => {
            notification.style.display = 'none';
        }, 3000);
    }

    async loadHistory() {
        try {
            const response = await fetch('/api/oracle/history');
            const data = await response.json();
            
            if (data.success) {
                return data.history;
            } else {
                throw new Error(data.message || 'Không thể tải lịch sử');
            }
        } catch (error) {
            console.error('History load error:', error);
            return null;
        }
    }

    formatHistoryDisplay(historyText) {
        if (!historyText || historyText.trim() === '') {
            return '<p>Chưa có lịch sử xem quẻ nào.</p>';
        }

        // Split by the separator lines and format each entry
        const entries = historyText.split('============================================================');
        const formattedEntries = entries
            .filter(entry => entry.trim() !== '')
            .map(entry => {
                const lines = entry.trim().split('\n');
                const timeLine = lines.find(line => line.includes('THỜI GIAN:'));
                const nameLine = lines.find(line => line.includes('TÊN:'));
                const categoryLine = lines.find(line => line.includes('LOẠI QUẺ:'));
                const oracleLine = lines.find(line => line.includes('PHÁN:'));
                const thuyLinhLine = lines.find(line => line.includes('LỜI NHẮN TỪ ĐẠI PHÁP SƯ THÙY LINH:'));

                if (timeLine && nameLine && categoryLine && oracleLine) {
                    const time = timeLine.replace('THỜI GIAN:', '').trim();
                    const name = nameLine.replace('TÊN:', '').trim();
                    const category = categoryLine.replace('LOẠI QUẺ:', '').trim();
                    const oracle = oracleLine.replace('PHÁN:', '').trim();
                    const thuyLinhMessage = thuyLinhLine ? thuyLinhLine.replace('LỜI NHẮN TỪ ĐẠI PHÁP SƯ THÙY LINH:', '').trim() : '';

                    return `
                        <div class="history-entry" style="margin-bottom: 1.5rem; padding: 1rem; background: rgba(255,255,255,0.5); border-radius: 10px;">
                            <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                                <strong>${name}</strong>
                                <span style="color: #6B7280; font-size: 0.9rem;">${time}</span>
                            </div>
                            <div style="color: #4F46E5; font-weight: 600; margin-bottom: 0.5rem;">${category}</div>
                            <div style="font-style: italic; margin-bottom: 0.5rem;">"${oracle}"</div>
                            ${thuyLinhMessage ? `<div style="color: #FFD700; font-size: 0.9rem; font-style: italic;">🌟 ${thuyLinhMessage}</div>` : ''}
                        </div>
                    `;
                }
                return '';
            })
            .filter(entry => entry !== '');

        return formattedEntries.join('');
    }
}

// Global functions for button actions
function shareOracle() {
    const oracleText = document.getElementById('oracleText').textContent;
    const thuyLinhText = document.getElementById('thuyLinhText').textContent;
    const userName = document.getElementById('resultName').textContent;
    const category = document.getElementById('resultCategory').textContent;
    
    const shareText = `🔮 ${category} 🔮\n\nNgười xem: ${userName}\n\nLời phán: "${oracleText}"\n\n🌟 Lời nhắn từ Đại Pháp Sư Thùy Linh: "${thuyLinhText}"\n\n🌟 TECH ORACLE 2026 - Đại Pháp Sư Thùy Linh`;
    
    if (navigator.share) {
        navigator.share({
            title: 'TECH ORACLE 2026',
            text: shareText
        }).catch(err => console.log('Share failed:', err));
    } else {
        // Fallback: Copy to clipboard
        navigator.clipboard.writeText(shareText).then(() => {
            oracleApp.showNotification('Đã sao chép vào clipboard!', 'success');
        }).catch(() => {
            // Fallback: Create temporary textarea
            const textarea = document.createElement('textarea');
            textarea.value = shareText;
            document.body.appendChild(textarea);
            textarea.select();
            document.execCommand('copy');
            document.body.removeChild(textarea);
            oracleApp.showNotification('Đã sao chép vào clipboard!', 'success');
        });
    }
}

async function viewHistory() {
    const historySection = document.getElementById('historySection');
    const historyContent = document.getElementById('historyContent');
    
    historyContent.innerHTML = '<p>Đang tải lịch sử...</p>';
    historySection.style.display = 'block';
    
    const history = await oracleApp.loadHistory();
    
    if (history !== null) {
        historyContent.innerHTML = oracleApp.formatHistoryDisplay(history);
    } else {
        historyContent.innerHTML = '<p>Không thể tải lịch sử. Vui lòng thử lại!</p>';
    }
    
    historySection.scrollIntoView({ behavior: 'smooth', block: 'center' });
}

function closeHistory() {
    const historySection = document.getElementById('historySection');
    historySection.style.display = 'none';
}

function newReading() {
    const resultSection = document.getElementById('oracleResult');
    resultSection.style.display = 'none';
    
    // Scroll to crystal ball
    document.getElementById('crystalBall').scrollIntoView({ behavior: 'smooth', block: 'center' });
}

// Initialize the app when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.oracleApp = new OracleApp();
    
    // Add some initial animations
    setTimeout(() => {
        oracleApp.showNotification(' Chào mừng đến với TECH ORACLE 2026 - Đại Pháp Sư Thùy Linh!', 'success');
    }, 1000);
});

// Add keyboard shortcuts
document.addEventListener('keydown', (e) => {
    if (e.ctrlKey || e.metaKey) {
        switch(e.key) {
            case 'h':
                e.preventDefault();
                viewHistory();
                break;
            case 'n':
                e.preventDefault();
                newReading();
                break;
            case 's':
                e.preventDefault();
                if (oracleApp.currentOracle) {
                    shareOracle();
                }
                break;
        }
    }
});

// Add touch support for mobile
let touchStartY = 0;
let touchEndY = 0;

document.addEventListener('touchstart', (e) => {
    touchStartY = e.changedTouches[0].screenY;
});

document.addEventListener('touchend', (e) => {
    touchEndY = e.changedTouches[0].screenY;
    handleSwipe();
});

function handleSwipe() {
    const swipeDistance = touchStartY - touchEndY;
    const minSwipeDistance = 50;
    
    if (Math.abs(swipeDistance) > minSwipeDistance) {
        if (swipeDistance > 0) {
            // Swipe up - could trigger new reading
            if (oracleApp.currentOracle) {
                newReading();
            }
        } else {
            // Swipe down - could show history
            viewHistory();
        }
    }
}

// Console welcome message
console.log('%c🔮 TECH ORACLE 2026 - Đại Pháp Sư Thùy Linh', 'color: #FFD700; font-size: 16px; font-weight: bold;');
console.log('%cPowered by Python Flask & JavaScript', 'color: #00CED1; font-size: 14px;');
console.log('%cKeyboard shortcuts: Ctrl+H (History), Ctrl+N (New), Ctrl+S (Share)', 'color: #FF1493; font-size: 12px;');
