from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import json
from datetime import datetime
import random

app = Flask(__name__)

# Oracle data - 180 cards divided into 6 categories
ORACLE_DATA = {
    "vận_may": [
        "Vận may của bạn đang load 99% thì bị rớt mạng, nhưng đừng lo, vũ trụ sẽ auto-reconnect cho bạn sớm thôi!",
        "Hôm nay bạn là Admin của cuộc đời, có quyền ban hành bug và deploy hạnh phúc vào hệ thống tâm hồn.",
        "Đời bạn đang bị dính virus xui xẻo, cần quét lại bằng nụ cười và restart lại thái độ sống.",
        "Vận may đang được backup trên cloud của vũ trụ, có thể mất vài giây để sync xuống thực tại.",
        "Hôm nay CPU của bạn chạy ở 100% hiệu suất, mọi dự định đều sẽ được execute thành công.",
        "Vận may của bạn đang trong chế độ Maintenance để upgrade phiên bản 'Rực Rỡ 2.0'.",
        "Bạn vừa nhận được update Vận may phiên bản 2026, tính năng mới: 'Không thể thất bại'.",
        "Hệ thống Vận may của bạn đang được nâng cấp với AI 'Thấu Hiểu Tim Hồn'.",
        "Vận may đang được cài đặt, đừng tắt máy hy vọng, process đang chạy ở background.",
        "Hôm nay bạn có quyền truy cập root vào kho báu vận may, mật khẩu: 'tin-tot-va-ban-linh'.",
        "Vận may của bạn đang được optimize bằng thuật toán 'Tâm Tĩnh Tự An'.",
        "Bạn vừa unlock thành tựu 'May Mắn Bùng Nổ' + 'Hạnh Phúc Vô Tận'.",
        "Vận may đang được sync với đa vũ trụ, tín hiệu mạnh: 5G của hạnh phúc.",
        "Hôm nay lucky item của bạn: Nụ cười + 1000cc tự tin, hiệu quả 200%.",
        "Vận may của bạn đang được cache vào RAM của vũ trụ, tốc độ truy xuất tức thì.",
        "Bạn đang trong top trending của thần may mắn, hashtag: #CuocSongToiSang #ThanhCongRucRo.",
        "Vận may của bạn đang được distributed đến mọi timeline, từ quá khứ đến tương lai.",
        "Hôm nay bạn có admin quyền trong cuộc sống, có thể edit bất kỳ kịch bản nào.",
        "Vận may đang được load từ server 'Thiên Thần Hộ Mệnh', ping: 1ms.",
        "Bạn vừa nhận được VIP pass của vận may, quyền lợi: không bao giờ thất bại.",
        "Vận may của bạn đang được encrypted bằng khóa 'Tâm Thiện An Lành'.",
        "Hôm nay bạn có firewall chống xui xẻo version 'Diamond Plus'.",
        "Vận may đang được compress để tối ưu không gian hạnh phúc trong tim bạn.",
        "Bạn vừa nhận được patch vá lỗi 'Luôn C Đúng Thời Điểm'.",
        "Vận may của bạn đang được clone thành nhiều bản sao để chia sẻ cho mọi người.",
        "Hôm nay bạn có unlimited access đến kho báu may mắn của vũ trụ.",
        "Vận may đang được debug bởi Đại Pháp Sư Thùy Linh, kết quả: Perfect!",
        "Bạn vừa nhận được beta key của vận may phiên bản 'Đỉnh Cao Chóp'.",
        "Vận may của bạn đang được test trên môi trường production của thiên đường.",
        "Hôm nay bạn là MOD của diễn đàn may mắn, có quyền ban vận xui."
    ],
    "tình_duyên": [
        "Trái tim bạn không phải là mã nguồn mở, đừng để ai cũng vào Fork rồi để lại Bug. Hãy chờ người xứng đáng Commit cả đời với bạn.",
        "Crush đang set chế độ Private với bạn, nhưng đừng lo, tình yêu thực sự không cần Public, chỉ cần hai người thấy là đủ.",
        "Tình duyên dính Bug, người yêu cũ đang gửi yêu cầu kết nối lại. Hãy chạy antivirus 'Quên Qua' và install 'Tương Lai Tươi Sáng'.",
        "Trái tim bạn đang bị lag, cần restart lại cảm xúc. Đừng Force Quit tình yêu, hãy thử Safe Mode một thời gian.",
        "Crush đang online nhưng ẩn giấu cảm xúc, giống như API không có documentation. Hãy kiên nhẫn explore nhé!",
        "Tình duyên của bạn đang trong chế độ Safe Mode, đang bảo vệ khỏi những mối quan hệ không an toàn.",
        "Bạn vừa nhận được friend request từ định mệnh, accept ngay đi, đừng để expire!",
        "Tình yêu đang được cài đặt lại từ đầu, version mới có tính năng 'Bất Ly Bệt'.",
        "Crush đang buffer, đừng đóng tab cảm xúc. Tình yêu cần thời gian để load hết vẻ đẹp.",
        "Tình duyên của bạn đang được update, patch mới: 'Hiểu và Chia Sẻ'.",
        "Bạn đang có 99+ tin nhắn chưa đọc từ vũ trụ, nội dung: 'Bạn xứng đáng với tình yêu tuyệt vời'.",
        "Tình yêu đang được optimize cho hiệu suất tốt hơn, giảm lag và tăng FPS hạnh phúc.",
        "Crush đang xem story của bạn 10 lần/ngày, algorithm của tình yêu đang hoạt động rồi!",
        "Tình duyên đang được sync với tâm hồn bạn, mọi tín hiệu đều positive.",
        "Bạn vừa nhận được notification từ người thương: 'Tìm thấy bạn trong tương lai của tôi'.",
        "Tình yêu đang được backup vào memories, không bao giờ bị lost data nữa.",
        "Crush đang save ảnh của bạn vào folder ẩn tên 'Người Yêu Tương Lai'.",
        "Tình duyên đang được encrypt bằng nụ cười, chỉ có thể decrypt bằng trái tim chân thành.",
        "Bạn đang trong waiting list của hạnh phúc, sắp đến turn rồi!",
        "Tình yêu đang được load từ server tâm hồn, tốc độ: Gigabit của sự chân thành.",
        "Crush đang typing... nhưng không gửi gì, có thể đang soạn một bản tuyên ngôn tình yêu.",
        "Tình duyên đang được compress để tiết kiệm nước mắt, tăng dung lượng cho nụ cười.",
        "Bạn vừa nhận được love patch từ vũ trụ, tính năng: 'Tình Yêu Bất Tận'.",
        "Tình yêu đang được distributed đến mọi giác quan, bạn sẽ cảm nhận được từ mọi phía.",
        "Crush đang heart react mọi post của bạn, algorithm của Instagram cũng phải ghen tị.",
        "Tình duyên đang được cache trong ký ức, mỗi lần recall đều ngọt ngào.",
        "Bạn đang trong relationship status: 'Đang Chờ Người Xứng Đáng'.",
        "Tình yêu đang được debug bởi Cupid, kết quả: Compatible 100%!",
        "Crush đang follow bạn từ thế giới khác, có thể là twin flame từ parallel universe.",
        "Tình duyên đang được test A/B với hạnh phúc, version nào cũng thắng!"
    ],
    "sự_nghiệp": [
        "Sếp đang định Update lương cho bạn nhưng bị lỗi Server. Đừng lo, vũ trụ sẽ gửi bonus qua karma transfer.",
        "Sự nghiệp thăng tiến như tốc độ SSD, mọi dự định đều được load trong tích tắc.",
        "Deadline đang đuổi theo bạn với tốc độ 1Gbps, nhưng bạn có VPN 'Thông Minh' để vượt qua.",
        "Sự nghiệp của bạn đang được optimize bằng algorithm 'Nỗ Lực Không Ngừng'.",
        "Sếp đang xem performance của bạn với 5 stars, comment: 'Nhân viên vàng của công ty'.",
        "Sự nghiệp đang được upgrade lên phiên bản Pro, tính năng: 'Thành Công Tự Động'.",
        "Bạn vừa nhận được promotion từ vũ trụ, chức vụ: 'Chiến Binh Hạnh Phúc'.",
        "Sự nghiệp đang được sync với tiềm năng của bạn, mọi indicator đều màu xanh lá.",
        "Deadline đang được extend theo yêu cầu của vũ trụ, bạn có thêm thời gian để tỏa sáng.",
        "Sự nghiệp của bạn đang được backup vào cloud của thành công, không bao giờ mất data.",
        "Bạn đang có unlimited PTO từ sếp, điều kiện: phải hạnh phúc mỗi ngày.",
        "Sự nghiệp đang được distributed thành công, mọi nỗ lực đều được nhân đôi hiệu quả.",
        "Sếp đang typing... email khen thưởng, có thể là tăng lương + bonus + cổ phiếu.",
        "Sự nghiệp đang được encrypt bằng nỗ lực, chỉ có thể decrypt bằng thành công.",
        "Bạn đang trong top performer của tháng, reward: sự ngưỡng mộ của đồng nghiệp.",
        "Sự nghiệp đang được cache vào CV của bạn, mỗi lần interview đều gây ấn tượng.",
        "Sếp đang save tên bạn vào folder 'Promotion List 2026', sắp đến lượt rồi!",
        "Sự nghiệp đang được compress bằng hiệu suất, giảm thời gian tăng gấp đôi kết quả.",
        "Bạn vừa nhận được bonus từ karma, số dư tài khoản may mắn: vô hạn.",
        "Sự nghiệp đang được debug bởi chuyên gia, không còn bug nào có thể ngăn cản bạn.",
        "Sếp đang heart react mọi report của bạn, dấu hiệu của sự thăng tiến sắp tới.",
        "Sự nghiệp đang được load từ cloud tài năng, bandwidth: không giới hạn.",
        "Bạn đang trong fast track của thành công, ETA: ngay bây giờ!",
        "Sự nghiệp đang được clone cho tương lai, version bạn của năm 2030 sẽ đỉnh hơn.",
        "Sếp đang follow profile LinkedIn của bạn, đang chuẩn bị offer không thể chối từ.",
        "Sự nghiệp đang được test với pressure, bạn pass với điểm tuyệt đối.",
        "Bạn vừa unlock achievement 'Work-Life Balance Master'.",
        "Sự nghiệp đang được patch vá lỗi 'Chậm Tiến Độ', giờ thì tốc độ ánh sáng.",
        "Sếp đang recommend bạn cho CEO, tương lai: quản lý cấp cao!",
        "Sự nghiệp đang được distributed toàn cầu, bạn sắp trở thành global star!"
    ],
    "tiền_tài": [
        "Ví tiền đang báo lỗi 404: Not Found, nhưng vũ trụ đang redirect đến kho báu 200 OK.",
        "Tiền vào như nước nhưng thoát ra như RAM bị tràn. Đề xuất: upgrade ví lên version 'Không Giới Hạn'.",
        "Sắp có khoản thu nhập bất ngờ từ một nguồn Code cũ, có thể là side project bạn đã quên.",
        "Tài chính của bạn đang được optimize bằng AI 'Thu Hút Tài Lộc'.",
        "Ví tiền đang được update phiên bản Unlimited, tính năng: 'Tiền Tự Sinh Sôi'.",
        "Tiền đang được sync với tài khoản ngân hàng của vũ trụ, số dư: vô hạn.",
        "Bạn vừa nhận được bonus từ vũ trụ, amount: đủ để mua hạnh phúc trọn đời.",
        "Tài chính đang được backup vào savings của thiên đường, lãi suất: 1000%/năm.",
        "Tiền đang được cache vào ví điện tử của bạn, transaction fee: 0, happiness fee: 100%.",
        "Bạn đang có unlimited access đến wealth, mật khẩu: 'Nỗ Lực + Kiên Trì'.",
        "Tài chính đang được encrypt bằng thông minh, không hacker nào có thể đánh cắp may mắn.",
        "Tiền đang được distributed thành công đến mọi túi quần và ví của bạn.",
        "Bạn vừa nhận được financial patch từ vũ trụ, bug fix: 'Luôn Đủ Tiền'.",
        "Tài chính đang được debug bởi Warren Buffett, kết quả: Perfect Portfolio!",
        "Tiền đang được load từ investment cloud, returns: 1000x trong 1 năm.",
        "Bạn đang trong top trending của millionaires, hashtag: #GiauTuTuoiTre #ThanhCongRucRo.",
        "Tài chính đang được compress bằng tiết kiệm thông minh, tối ưu chi tiêu tối đa.",
        "Tiền đang được clone cho thế hệ sau, con cháu bạn sẽ là triệu phú thế hệ thứ 3.",
        "Bạn vừa unlock achievement 'Financial Freedom', reward: cuộc sống viên mãn.",
        "Tài chính đang được test với market volatility, bạn pass với flying colors.",
        "Tiền đang được sync với crypto của vũ trụ, coin: HạnhPhúcCoin (HPC).",
        "Bạn đang receive notification từ lottery, prize: cuộc sống không lo nghĩ.",
        "Tài chính đang được upgrade premium, features: 'Tiền Tự Động Tìm Đến'.",
        "Tiền đang được cached vào real estate, bạn sắp có bất động sản trên sao Hỏa.",
        "Bạn đang have VIP access to wealth, level: Diamond Plus Unlimited.",
        "Tài chính đang được distributed globally, bạn sắp trở thành billionaire.",
        "Tiền đang được optimized by AI 'Thần Tài', ROI: không thể tính hết.",
        "Bạn đang receive bonus from universe, amount: đủ để làm bất cứ điều gì bạn muốn.",
        "Tài chính đang been debug by Đại Pháp Sư Thùy Linh, kết quả: Vô Cùng Tài Lộc!"
    ],
    "sức_khỏe": [
        "Cơ thể bạn là Server duy nhất bạn có, đừng để nó Crash vì thiếu ngủ. Hãy Shutdown công việc và Reboot lại năng lượng ngay!",
        "Sức khỏe của bạn đang được backup trên cloud của vũ trụ, restore point: trạng thái lý tưởng.",
        "Hệ thống miễn dịch đang được update phiên bản 2026, tính năng: 'Chống Bệnh Tận Cùng'.",
        "Cơ thể đang được optimize bằng algorithm 'Sống Lành Mạnh Mỗi Ngày'.",
        "Bạn đang có unlimited energy từ vũ trụ, battery life: vô hạn.",
        "Sức khỏe đang được sync với thiên nhiên, mọi indicator đều màu xanh lá cây.",
        "Hormone hạnh phúc đang được distributed đến mọi tế bào, effect: cười không ngớt.",
        "Cơ thể đang được debug bởi bác sĩ thiên thần, kết quả: Perfect Health!",
        "Bạn đang trong top trending của người khỏe mạnh, hashtag: #SongKhoeDep #NangLuongVoTan.",
        "Sức khỏe đang được cache vào DNA của bạn, mỗi tế bào đều chứa năng lượng tích cực.",
        "Cơ thể đang được encrypt bằng sức mạnh tinh thần, không virus nào có thể xâm nhập.",
        "Bạn vừa nhận được health patch từ vũ trụ, features: 'Không Bao Giờ Mệt Mỏi'.",
        "Sức khỏe đang được load từ server 'Thiên Thần Hộ Mệnh', ping: 0.1ms.",
        "Cơ thể đang được test với stress test, bạn pass với điểm tuyệt đối.",
        "Bạn đang have unlimited access đến năng lượng, source: vũ trụ vô tận.",
        "Sức khỏe đang been optimized by AI 'Sống Thọ', tuổi thọ dự kiến: 150+.",
        "Cơ thể đang được distributed với sức mạnh, mỗi cơ bắp đều chứa năng lượng宇宙.",
        "Bạn vừa unlock achievement 'Master of Health', reward: cơ thể lý tưởng.",
        "Sức khỏe đang been debug bởi Đại Pháp Sư Thùy Linh, kết quả: Beyond Perfect!",
        "Cơ thể đang được sync với tâm hồn, harmony level: maximum.",
        "Bạn đang receive health bonus from karma, amount: đủ để sống 200 năm khỏe mạnh.",
        "Sức khỏe đang been upgraded to version 'Super Human 2.0'.",
        "Cơ thể đang been protected by shield 'Vô Song Kháng Lực'.",
        "Bạn đang have VIP access đến fountain of youth, level: Diamond.",
        "Sức khỏe đang been distributed đến mọi giác quan, bạn sẽ cảm nhận tuyệt vời.",
        "Cơ thể đang been optimized for longevity, aging process: slowed down 90%.",
        "Bạn đang receive continuous health updates from universe, status: Perfect!"
    ],
    "vũ_trụ": [
        "Vũ trụ đang gửi tín hiệu 200 OK đến bạn. Mọi khó khăn hiện tại chỉ là bước đệm để bạn Compile ra một phiên bản rực rỡ nhất.",
        "Thiên thần đang typing... message cho bạn: 'Bạn được chọn cho nhiệm vụ đặc biệt: làm cho thế giới này tốt đẹp hơn'.",
        "Vũ trụ đang backup kế hoạch của bạn vào cloud của định mệnh, đảm bảo không bao giờ mất data hạnh phúc.",
        "Galaxy đang sync với tâm hồn bạn, frequency: 528Hz - frequency của tình yêu và chữa lành.",
        "Bạn đang nhận được cosmic download, nội dung: 'Bí mật của vũ trụ đã được giải mã trong tim bạn'.",
        "Vũ trụ đang debug code của cuộc đời bạn, kết quả: Perfect! Không còn bug nào.",
        "Thiên thần đang deploy update cho cuộc đời bạn, version: 'Rực Rỡ Vô Tận 2026'.",
        "Bạn đang có admin access đến cosmic server, có thể edit bất kỳ reality nào.",
        "Vũ trụ đang gửi bạn cosmic notification: 'Mission accomplished! Ready for next level'.",
        "Stars đang align cho bạn, constellation: 'Thành Công Và Hạnh Phúc'.",
        "Bạn đang receive cosmic energy boost, power level: Over 9000!",
        "Vũ trụ đang compress wisdom cho bạn, file size: vô hạn, content: tất cả câu trả lời.",
        "Galaxy đang cache your dreams vào server của thực tại, chúng sắp thành sự thật.",
        "Bạn đang được connected đến cosmic internet, download speed: không giới hạn.",
        "Vũ trụ đang send bạn cosmic email với attachment: 'Bản đồ kho báu hạnh phúc'.",
        "Thiên thần đang monitor progress của bạn, status: Exceeding all expectations!",
        "Bạn đang have cosmic VIP pass, benefits: unlimited wishes, instant manifestation.",
        "Vũ trụ đang optimize your timeline, removing all delays and obstacles.",
        "Galaxy đang sync với your energy, resonance: perfect harmony achieved.",
        "Bạn đang receive cosmic upgrade, features: 'Thấu Hiểu Vạn Vật'.",
        "Vũ trụ đang send bạn cosmic signal: 'You are on the right path, keep going'.",
        "Stars đang celebrate your existence, cosmic party: happening now in your honor!",
        "Bạn đang connected đến cosmic consciousness, access level: Master.",
        "Vũ trụ đang send you cosmic love package, delivery: ngay lập tức!",
        "Galaxy đang align with your purpose, mission clarity: 100% achieved.",
        "Bạn đang receive cosmic wisdom download, format: direct soul transmission.",
        "Vũ trụ đang send you cosmic confirmation: 'You are loved, you are supported, you are enough'.",
        "Thiên thần đang prepare cosmic celebration for your achievements, date: every day!",
        "Bạn đang live in cosmic reality where everything is possible and you are the creator!"
    ]
}

# Messages from Đại Pháp Sư Thùy Linh
THUY_LINH_MESSAGES = [
    "Hãy tin vào sức mạnh của vũ trụ, nó luôn ở bên cạnh bạn.",
    "Mỗi ngày là một cơ hội để trở thành phiên bản tốt hơn của chính mình.",
    "Bạn mạnh mẽ hơn bạn nghĩ, vũ trụ biết điều đó.",
    "Hãy mỉm cười, vũ trụ đang mỉm cười lại với bạn.",
    "Thành công không phải đích đến, mà là hành trình bạn đang đi.",
    "Bạn xứng đáng với tất cả những điều tốt đẹp nhất.",
    "Hãy lắng nghe trái tim, vũ trụ đang nói chuyện qua đó.",
    "Mọi khó khăn đều là bài học để bạn trở nên mạnh mẽ hơn.",
    "Bạn là một ngôi sao sáng, đừng để ai làm bạn lụi tàn.",
    "Vũ trụ có kế hoạch tuyệt vời cho bạn, hãy tin tưởng.",
    "Hãy yêu thương bản thân trước khi yêu thương thế giới.",
    "Bạn được sinh ra để tỏa sáng, đừng che giấu ánh sáng của mình.",
    "Mỗi khoảnh khắc đều là món quà từ vũ trụ.",
    "Hãy sống trong hiện tại, đó là nơi phép màu xảy ra.",
    "Bạn có sức mạnh thay đổi thực tại của chính mình.",
    "Vũ trụ luôn hỗ trợ những người dám mơ lớn.",
    "Hãy kiên nhẫn, những điều tốt đẹp nhất cần thời gian.",
    "Bạn là hiện thân của tình yêu và ánh sáng.",
    "Mỗi bước đi bạn đều để lại dấu ấn trên vũ trụ.",
    "Hãy tin vào trực giác, đó là tiếng nói của vũ trụ.",
    "Bạn được bao quanh bởi năng lượng tích cực.",
    "Mọi thử thách đều làm bạn trở nên phi thường.",
    "Hãy sống cuộc đời mà bạn sẽ tự hào khi kể lại.",
    "Bạn là một kỳ quan, hãy tỏa sáng như vậy.",
    "Vũ trụ đang chờ đợi bạn tỏa sáng.",
    "Hãy là nguyên nhân của niềm vui, không phải kết quả.",
    "Bạn có tất cả những gì cần để thành công.",
    "Hãy tin vào quá trình, vũ trụ đang sắp xếp mọi thứ."
]

@app.route('/')
def index():
    """Main oracle page"""
    return render_template('index.html')

@app.route('/api/oracle/<category>')
def get_oracle(category):
    """Get random oracle from specified category"""
    try:
        if category not in ORACLE_DATA:
            return jsonify({
                'success': False,
                'message': 'Category not found'
            }), 400
        
        # Get random oracle from category
        oracle_text = random.choice(ORACLE_DATA[category])
        
        # Get random message from Đại Pháp Sư Thùy Linh
        thuy_linh_message = random.choice(THUY_LINH_MESSAGES)
        
        # Get user info from request
        user_data = {
            'name': request.args.get('name', 'Ẩn danh'),
            'birthday': request.args.get('birthday', 'Không rõ'),
            'zodiac': request.args.get('zodiac', 'Không rõ'),
            'category': category,
            'oracle': oracle_text,
            'thuy_linh_message': thuy_linh_message,
            'timestamp': datetime.now().isoformat()
        }
        
        # Log to file
        log_oracle_reading(user_data)
        
        return jsonify({
            'success': True,
            'oracle': oracle_text,
            'thuy_linh_message': thuy_linh_message,
            'category': category,
            'timestamp': user_data['timestamp']
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

def log_oracle_reading(user_data):
    """Log oracle reading to file"""
    try:
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Log entry
        log_entry = f"""
{'='*60}
THỜI GIAN: {user_data['timestamp']}
TÊN: {user_data['name']}
NGÀY SINH: {user_data['birthday']}
CUNG HOÀNG ĐẠO: {user_data['zodiac']}
LOẠI QUẺ: {user_data['category'].upper().replace('_', ' ')}
PHÁN: {user_data['oracle']}
LỜI NHẮN TỪ ĐẠI PHÁP SƯ THÙY LINH: {user_data['thuy_linh_message']}
{'='*60}
"""
        
        # Write to log file
        log_file = 'logs/oracle_120.log'
        with open(log_file, 'a', encoding='utf-8') as f:
            f.write(log_entry)
            
    except Exception as e:
        print(f"Error logging oracle reading: {str(e)}")

@app.route('/api/oracle/history')
def get_oracle_history():
    """Get oracle reading history"""
    try:
        log_file = 'logs/oracle_120.log'
        if not os.path.exists(log_file):
            return jsonify({
                'success': True,
                'history': []
            })
        
        with open(log_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        return jsonify({
            'success': True,
            'history': content
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/api/categories')
def get_categories():
    """Get all available categories"""
    categories = {
        'vận_may': 'VẬN MAY',
        'tình_duyên': 'TÌNH DUYÊN',
        'sự_nghiệp': 'SỰ NGHIỆP',
        'tiền_tài': 'TIỀN TÀI',
        'sức_khỏe': 'SỨC KHỎE',
        'vũ_trụ': 'VŨ TRỤ GỬI THÔNG ĐIỆP'
    }
    return jsonify(categories)

@app.route('/static/<path:filename>')
def static_files(filename):
    """Serve static files"""
    return send_from_directory('static', filename)

@app.route('/api/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat(),
        'oracle_count': sum(len(oracles) for oracles in ORACLE_DATA.values())
    })

if __name__ == '__main__':
    # Check if running on Render.com
    if os.environ.get('RENDER'):
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)
    else:
        # Local development
        print("🔮 BẮT ĐẦU TECH ORACLE 2026 - ĐẠI PHÁP SƯ THÙY LINH...")
        print("🌐 Server available at: http://localhost:5000")
        
        # Create necessary directories
        if not os.path.exists('templates'):
            os.makedirs('templates')
        if not os.path.exists('static'):
            os.makedirs('static')
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        app.run(host='0.0.0.0', port=5000, debug=True)
