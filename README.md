# 🔮 TECH ORACLE 2026 - Đại Pháp Sư Thùy Linh

> 🌟 Ứng dụng bói toán định mệnh công nghệ với 180 quẻ mystical và giao diện neon rực rỡ

## ✨ Features

- 🎴 **180 Oracle Cards** (6 chủ đề × 30 câu mỗi chủ đề)
- 🎨 **6 Nút Neon** với hiệu ứng hover cực đẹp
- ⌨️ **Typewriter Effect** - chữ hiện ra từ từ như đang gõ phím
- 🌟 **Messages từ Đại Pháp Sư Thùy Linh** - 30 lời nhắn ngẫu nhiên
- 📱 **Responsive Design** - hoạt động hoàn hảo trên mọi thiết bị
- 📝 **History Tracking** - lưu lại tất cả lần xem quẻ
- 📤 **Share Functionality** - chia sẻ kết quả với bạn bè
- ⌨️ **Keyboard Shortcuts** - Ctrl+H, Ctrl+N, Ctrl+S

## 🎯 6 Chủ Đề Oracle

| Chủ đề | Màu Neon | Icon | Số lượng |
|---------|------------|-------|-----------|
| **VẬN MAY** | 🌸 Pink | 🌟 | 30 câu |
| **TÌNH DUYÊN** | 💙 Blue | 💕 | 30 câu |
| **SỰ NGHIỆP** | 💚 Green | 🚀 | 30 câu |
| **TIỀN TÀI** | 💛 Yellow | 💰 | 30 câu |
| **SỨC KHỎE** | 🧧 Orange | 💪 | 30 câu |
| **VŨ TRỤ GỬI THÔNG ĐIỆP** | 💜 Purple | 🌌 | 30 câu |

## 🚀 Quick Start (Local)

### Prerequisites
- Python 3.9+
- pip

### Installation
```bash
# Clone repository
git clone <your-repo-url>
cd tech-oracle-2026

# Install dependencies
pip install -r requirements.txt

# Run server
python app.py
```

### Access
Open browser: http://localhost:5000

## 🌐 Deploy to Render.com

### Step 1: Prepare Files
Tất cả files đã sẵn sàng:
- ✅ `app.py` - Flask application
- ✅ `requirements.txt` - Dependencies + gunicorn
- ✅ `Procfile` - Gunicorn configuration
- ✅ `runtime.txt` - Python 3.9.19
- ✅ `.gitignore` - Ignore unnecessary files

### Step 2: Push to GitHub
```bash
# Initialize git
git init
git add .
git commit -m "Tech Oracle 2026 - Ready for Render"

# Create repository on GitHub first, then:
git remote add origin https://github.com/yourusername/tech-oracle-2026.git
git branch -M main
git push -u origin main
```

### Step 3: Deploy to Render
1. **Vào [Render.com](https://render.com)**
2. **Đăng nhập** bằng GitHub
3. **Click "New +" → "Web Service"**
4. **Connect GitHub repository**
5. **Render sẽ tự động detect:**
   - Runtime: Python
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
6. **Click "Create Web Service"**

### Step 4: Configuration
Render sẽ tự động cấu hình:
- **Name**: tech-oracle-2026
- **Region**: Singapore (hoặc nearest)
- **Branch**: main
- **Root Directory**: ./
- **Instance Type**: Free (hoặc paid)

### Step 5: Access App
Sau khi deploy thành công:
- **URL**: `https://tech-oracle-2026.onrender.com`
- **Logs**: Available trên Render dashboard
- **Auto-deploy**: Mỗi khi push code lên main branch

## 📁 Project Structure

```
tech-oracle-2026/
├── app.py                 # Flask application
├── requirements.txt         # Python dependencies
├── Procfile               # Render process configuration
├── runtime.txt            # Python version
├── .gitignore            # Git ignore rules
├── README.md              # This file
├── templates/
│   └── index.html        # HTML template
├── static/
│   ├── style.css         # Neon UI styles
│   └── script.js         # JavaScript with typewriter
└── logs/                 # Oracle history (auto-created)
```

## 🔧 Configuration

### Environment Variables (Render)
- `PORT` - Tự động set bởi Render
- `RENDER` - Detection flag cho production mode

### Local Development
```bash
# Development mode
python app.py
# Features: debug=True, port=5000
```

## 🎮 Usage Guide

### 1. Điền thông tin
- **Họ tên**: Tên của người xem quẻ
- **Ngày sinh**: Để tính tuổi và vận mệnh
- **Cung hoàng đạo**: 12 cung phổ biến

### 2. Chọn chủ đề
- Click vào 1 trong 6 nút neon
- Mỗi nút có màu và icon riêng
- Crystal ball sẽ đổi màu tương ứng

### 3. Nhận kết quả
- **Typewriter effect**: Chữ hiện từ từ
- **Oracle text**: Lời phán mystical
- **Thùy Linh message**: Lời nhắn đặc biệt
- **User info**: Hiển thị thông tin người xem

### 4. Tương tác
- **📤 Share**: Chia sẻ kết quả
- **📜 History**: Xem lịch sử xem quẻ
- **🔄 New**: Xem quẻ mới

## 🎨 Tech Stack

### Backend
- **Flask 2.3.3** - Python web framework
- **Gunicorn 21.2.0** - Production WSGI server
- **Python 3.9.19** - Runtime

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Neon effects, animations
- **JavaScript ES6+** - Typewriter, API calls

### Features
- **Glass morphism design**
- **Neon glow effects**
- **Responsive grid layout**
- **Smooth animations**
- **Touch/swipe support**

## 📊 API Endpoints

### Main Routes
- `GET /` - Main oracle interface
- `GET /api/oracle/<category>` - Get random oracle
- `GET /api/oracle/history` - Get reading history
- `GET /api/categories` - Get all categories
- `GET /api/health` - Health check

### Response Format
```json
{
  "success": true,
  "oracle": "Lời phán mystical...",
  "thuy_linh_message": "Lời nhắn từ Đại Pháp Sư Thùy Linh...",
  "category": "vận_may",
  "timestamp": "2026-03-30T01:30:00"
}
```

## 🔧 Troubleshooting

### Common Issues
1. **Build failed**: Check requirements.txt versions
2. **Port error**: Ensure port 5000 not in use
3. **Static files**: Check file paths in templates
4. **Logs not saving**: Check logs directory permissions

### Debug Mode
```bash
# Local development with debug
python app.py
# Access: http://localhost:5000
# Debug features: auto-reload, error pages
```

### Production Logs
```bash
# View Render logs
# 1. Go to Render dashboard
# 2. Select your service
# 3. Click "Logs" tab
# 4. Check for errors
```

## 🎯 Performance Optimization

### Frontend
- **Lazy loading** cho images
- **Minified CSS/JS**
- **Responsive images**
- **Cache headers**

### Backend
- **Gunicorn workers** optimization
- **Static file serving**
- **Database indexing** (if needed)
- **CDN integration**

## 🔒 Security

### Implemented
- **Input validation** cho user data
- **XSS protection** với Jinja2
- **CSRF protection** (Flask-WTF)
- **File path validation**

### Best Practices
- **Environment variables** cho sensitive data
- **HTTPS** trên production
- **Rate limiting** cho API calls
- **Regular updates** cho dependencies

## 🤝 Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push branch: `git push origin feature/amazing-feature`
5. Create Pull Request

## 📄 License

MIT License - Feel free to use, modify, and distribute

## 🙏 Acknowledgments

- **Flask** - Web framework
- **Render** - Hosting platform
- **Google Fonts** - Inter & Playfair Display
- **Font Awesome** - Icons (if used)

## 📞 Contact

- **Author**: Đại Pháp Sư Thùy Linh
- **Email**: [your-email@example.com]
- **Website**: [your-website.com]
- **GitHub**: [github.com/yourusername]

---

## 🔮 Oracle Messages Examples

### VẬN MAY
> "Vận may của bạn đang load 99% thì bị rớt mạng, nhưng đừng lo, vũ trụ sẽ auto-reconnect cho bạn sớm thôi!"

### TÌNH DUYÊN  
> "Trái tim bạn không phải là mã nguồn mở, đừng để ai cũng vào Fork rồi để lại Bug. Hãy chờ người xứng đáng Commit cả đời với bạn."

### SỨC KHỎE
> "Cơ thể bạn là Server duy nhất bạn có, đừng để nó Crash vì thiếu ngủ. Hãy Shutdown công việc và Reboot lại năng lượng ngay!"

### VŨ TRỤ GỬI THÔNG ĐIỆP
> "Vũ trụ đang gửi tín hiệu 200 OK đến bạn. Mọi khó khăn hiện tại chỉ là bước đệm để bạn Compile ra một phiên bản rực rỡ nhất."

---

**🌟 Tech Oracle 2026 - Nơi công nghệ gặp góc nhìn mystical!**
- **Navigation mượt** - Smooth scrolling và active link highlighting
- **Skill bars** - Hiển thị kỹ năng với animation
- **Project showcase** - Trưng bày dự án một cách chuyên nghiệp

## 📁 Cấu Trúc Thư Mục

```
portfolio/
├── app.py                 # Flask server
├── requirements.txt       # Python dependencies
├── README.md             # Documentation
├── templates/
│   └── index.html        # Main HTML file
├── static/
│   ├── style.css         # Stylesheet
│   └── script.js         # JavaScript file
└── contacts/             # Contact form submissions (created automatically)
```

## 🛠️ Cài Đặt

1. **Clone hoặc tải về dự án**
   ```bash
   # Nếu sử dụng git
   git clone <repository-url>
   cd portfolio
   ```

2. **Cài đặt Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Chạy server Flask**
   ```bash
   python app.py
   ```

4. **Mở trình duyệt**
   Truy cập http://localhost:5000

## 📝 Tùy Chỉnh

### Thông tin cá nhân

Mở file `templates/index.html` và thay đổi các thông tin sau:

1. **Tên của bạn**:
   ```html
   <h1>Xin Chào, Tôi Là <span class="highlight">[Tên Của Bạn]</span></h1>
   ```

2. **Thông tin trong section Giới thiệu**:
   ```html
   <div class="info-item">
       <strong>Tên:</strong> [Tên của bạn]
   </div>
   <div class="info-item">
       <strong>Email:</strong> email@example.com
   </div>
   <div class="info-item">
       <strong>Địa điểm:</strong> [Thành phố của bạn]
   </div>
   ```

3. **Thông tin liên hệ**:
   ```html
   <div class="contact-item">
       <strong>Email:</strong> email@example.com
   </div>
   <div class="contact-item">
       <strong>Phone:</strong> +84 123 456 789
   </div>
   <div class="contact-item">
       <strong>Location:</strong> [Thành phố của bạn], Việt Nam
   </div>
   ```

### Kỹ năng

Trong section Skills, bạn có thể điều chỉnh:

- Tên kỹ năng
- Mức độ (thay đổi width trong skill-bar)
- Icon emoji

### Dự án

Trong section Projects, cập nhật:

- Tên dự án
- Mô tả
- Công nghệ sử dụng
- Link demo và GitHub

### Màu sắc

Mở file `static/style.css` và điều chỉnh các biến CSS trong `:root`:

```css
:root {
    --primary-color: #4F46E5;
    --secondary-color: #10B981;
    --accent-color: #F59E0B;
    /* ... */
}
```

## 🔧 Flask Server

Server Flask có các endpoints:

- `GET /` - Trang chính
- `POST /api/contact` - Xử lý form liên hệ
- `GET /api/health` - Health check

### Contact Form

Khi người dùng điền form liên hệ:
1. Dữ liệu được validate
2. Lưu vào file `contacts/contact_[timestamp].txt`
3. Trả về JSON response
4. Hiển thị notification cho người dùng

## 🎨 Design Features

### Responsive Design
- Mobile-first approach
- Breakpoints tại 768px và 480px
- Hamburger menu cho mobile

### Animations
- Fade-in effects on scroll
- Typing effect cho hero title
- Skill bar animations
- Parallax scrolling

### Interactions
- Smooth scrolling navigation
- Active link highlighting
- Hover effects
- Form validation
- Toast notifications

## 🚀 Deployment

### Heroku
1. Tạo file `Procfile`:
   ```
   web: python app.py
   ```

2. Deploy:
   ```bash
   heroku create your-portfolio-name
   git push heroku main
   ```

### Vercel (cho frontend)
1. Chỉ cần upload folder `static/` và `templates/`
2. Cấu hình serverless function cho API

## 📱 Mobile Optimization

- Touch-friendly navigation
- Optimized images
- Fast loading times
- Readable fonts

## 🐛 Debug

- Enable debug mode trong `app.py`
- Check browser console
- View Flask logs
- Test contact form functionality

## 📄 License

MIT License - Feel free to use this template for your portfolio!

## 🤝 Contributing

1. Fork dự án
2. Tạo feature branch
3. Commit changes
4. Push to branch
5. Open Pull Request

---

**Happy Coding! 🎉**
