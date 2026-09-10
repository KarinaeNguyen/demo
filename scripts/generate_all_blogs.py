"""
Script to generate 24 SEO-optimized, Newsletter-style blog posts for Quoc Phan Design (quocphan.vn)
With semantic <image> placeholder tags and structured data.
"""

import os
import json
import re

BLOG_POSTS = [
    {
        "id": 1,
        "slug": "don-vi-san-xuat-noi-that-quan-binh-thanh-2024.html",
        "title": "Đơn Vị Sản Xuất Nội Thất Quận Bình Thạnh 2024 – Uy Tín & Trực Tiếp Tại Xưởng",
        "category": "Xưởng Sản Xuất",
        "date": "20/11/2023",
        "iso_date": "2023-11-20",
        "read_time": "5 phút đọc",
        "edition": "Số 01 • Chuyên đề Xưởng Gỗ & Thi Công",
        "meta_desc": "Công Ty TNHH Thiết Kế Quốc Phan - Đơn vị sản xuất nội thất Quận Bình Thạnh uy tín, may đo đồ gỗ tủ bếp, căn hộ, chung cư trực tiếp tại xưởng không qua trung gian.",
        "keywords": "đơn vị sản xuất nội thất quận bình thạnh, xưởng gỗ bình thạnh, thi công nội thất bình thạnh, nội thất quốc phan",
        "lead": "Khi tìm kiếm đơn vị sản xuất nội thất tại Quận Bình Thạnh, gia chủ luôn mong muốn tìm được một xưởng mộc làm việc bằng cái tâm, tay nghề chuẩn xác và biến từng bản vẽ 3D thành hiện thực bền đẹp với giá gốc trực tiếp từ xưởng.",
        "toc": [
            ("sec-1", "I. Quốc Phan Design – Đơn vị sản xuất nội thất uy tín tại Bình Thạnh"),
            ("sec-2", "II. Thiết kế độc đáo – Phản ánh đậm nét cá tính gia chủ"),
            ("sec-3", "III. Dịch vụ thi công chuyên nghiệp & chính sách bảo hành tận tâm"),
            ("sec-4", "IV. Cam kết vật liệu chuẩn An Cường & tiến độ bàn giao chính xác")
        ],
        "content_html": """
            <p><strong>Quốc Phan</strong> là thương hiệu chuyên sâu về thiết kế và trực tiếp sản xuất nội thất tại Quận Bình Thạnh với hơn 7 năm kinh nghiệm thực chiến. Chúng tôi sở hữu xưởng mộc quy mô trang bị hệ thống máy CNC tự động, chuyên biến mọi ý tưởng thiết kế căn hộ, nhà phố và tủ bếp thành không gian sống tiện nghi, đẳng cấp.</p>

            <h2 id="sec-1">I. Quốc Phan Design – Đơn vị sản xuất nội thất uy tín tại Bình Thạnh</h2>
            <p>Chúng tôi thấu hiểu rằng khi tìm kiếm đơn vị sản xuất nội thất Quận Bình Thạnh, bạn đang tìm kiếm một đối tác tin cậy: không chỉ có năng lực sản xuất máy móc hiện đại mà đội ngũ thợ mộc phải giàu kinh nghiệm, tỉ mỉ trong từng đường dán cạnh nẹp, bản lề giảm chấn đến nước sơn hoàn thiện.</p>
            <p>Với lợi thế xưởng sản xuất đặt ngay tại Bình Quới, Quận Bình Thạnh, chúng tôi luôn sẵn sàng mời khách hàng ghé thăm trực tiếp xưởng để kiểm tra chất lượng phôi gỗ, phụ kiện và quy trình gia công thực tế trước khi lắp đặt tại công trình.</p>

            <!-- <image src="" alt="Nội thất tủ bếp tại Bình Thạnh – Đơn vị sản xuất nội thất quận bình thạnh" /> -->

            <h2 id="sec-2">II. Thiết kế độc đáo – Phản ánh đậm nét cá tính gia chủ</h2>
            <p>Mỗi ngôi nhà là một câu chuyện riêng biệt, biểu tượng cho phong cách sống và gu thẩm mỹ của chủ nhân. Đội ngũ kiến trúc sư tại Quốc Phan không áp dụng các mẫu thiết kế rập khuôn có sẵn ngoài thị trường, mà dành thời gian lắng nghe thói quen sinh hoạt của từng thành viên để đưa ra giải pháp:</p>
            <ul>
                <li><strong>Tối ưu hóa công năng lưu trữ:</strong> Hệ tủ bếp kịch trần, tủ áo âm tường cánh lùa, giường ngủ thông minh tích hợp ngăn kéo.</li>
                <li><strong>Cập nhật vật liệu bề mặt mới nhất:</strong> Bề mặt Melamine chống trầy, Acrylic bóng gương sang trọng, Laminate vân gỗ tự nhiên và sơn 2K cao cấp.</li>
                <li><strong>Đảm bảo tính trung thực về vật liệu:</strong> Cam kết 100% phôi gỗ công nghiệp MDF lõi xanh chống ẩm chuẩn An Cường hoặc Ba Thanh chính hãng, minh bạch mã số màu gỗ.</li>
            </ul>

            <!-- <image src="" alt="Tủ bếp acrylic hiện đại sang trọng tại Bình Thạnh – Đơn vị sản xuất nội thất quận bình thạnh" /> -->

            <h2 id="sec-3">III. Dịch vụ thi công chuyên nghiệp & chính sách bảo hành tận tâm</h2>
            <p>Sự chuyên nghiệp của Quốc Phan không dừng lại ở khâu đóng đồ gỗ mà thể hiện xuyên suốt từ quá trình khảo sát hiện trạng công trình, lên bản vẽ chi tiết 2D/3D cho đến công tác bọc màng PE bảo vệ sản phẩm, vận chuyển và thi công lắp ráp sạch sẽ, an toàn.</p>
            <blockquote>
                "Chính sách bảo hành kết cấu gỗ lên tới 5 năm và bảo trì phụ kiện trọn đời là lời khẳng định vững chắc nhất cho chất lượng đồ gỗ xuất xưởng từ Quốc Phan Design."
            </blockquote>

            <!-- <image src="" alt="Tủ bếp melamine tại Bình Thạnh – Đơn vị sản xuất nội thất quận bình thạnh" /> -->

            <h2 id="sec-4">IV. Cam kết vật liệu chuẩn An Cường & tiến độ bàn giao chính xác</h2>
            <p>Khi lựa chọn đặt may đo nội thất trực tiếp tại xưởng Quốc Phan, khách hàng tiết kiệm được từ 20% đến 30% chi phí trung gian so với các showroom thương mại. Bạn hoàn toàn chủ động theo dõi tiến độ sản xuất và được đội ngũ KTS đồng hành trực tiếp từ đầu đến khi trao chìa khóa bàn giao công trình.</p>

            <!-- <image src="" alt="Tủ bếp laminate hiện đại tại Bình Thạnh – Đơn vị sản xuất nội thất quận bình thạnh" /> -->
        """
    },
    {
        "id": 2,
        "slug": "xuong-san-xuat-tu-bep-binh-thanh-2024.html",
        "title": "Xưởng Sản Xuất Tủ Bếp Bình Thạnh 2024 – May Đo Trực Tiếp, Bền Đẹp Chuẩn Bản Vẽ",
        "category": "Tủ Bếp",
        "date": "22/11/2023",
        "iso_date": "2023-11-22",
        "read_time": "6 phút đọc",
        "edition": "Số 02 • Cẩm Nang Bếp Thông Minh",
        "meta_desc": "Xưởng sản xuất tủ bếp Bình Thạnh 2024 - Quốc Phan Design chuyên đóng tủ bếp Acrylic, Melamine, MDF lõi xanh chống ẩm theo yêu cầu, phụ kiện thông minh Hafele Blum.",
        "keywords": "xưởng sản xuất tủ bếp bình thạnh, đóng tủ bếp bình thạnh, tủ bếp acrylic bình thạnh, tủ bếp gỗ công nghiệp chống ẩm",
        "lead": "Tủ bếp là trái tim của ngôi nhà. Đặt may đo tủ bếp trực tiếp tại xưởng Bình Thạnh giúp bạn sở hữu tam giác công năng hoàn hảo, chống ẩm mốc tuyệt đối và tiết kiệm ngân sách đáng kể.",
        "toc": [
            ("sec-1", "1. Lợi thế vị trí xưởng sản xuất tủ bếp Bình Thạnh"),
            ("sec-2", "2. Các dòng chất liệu tủ bếp được ưa chuộng nhất 2024"),
            ("sec-3", "3. Bố trí tam giác công năng bếp chuẩn khoa học"),
            ("sec-4", "4. Quy trình đóng tủ bếp tại xưởng Quốc Phan")
        ],
        "content_html": """
            <p>Trong xu hướng nội thất nhà ở hiện đại, phòng bếp không chỉ là nơi nấu nướng mà còn là không gian gắn kết gia đình. Tìm kiếm một <strong>xưởng sản xuất tủ bếp Bình Thạnh</strong> uy tín giúp gia chủ giải quyết triệt để nỗi lo cong vênh, ẩm mốc và kích thước không vừa vặn với góc tường.</p>

            <h2 id="sec-1">1. Lợi thế vị trí xưởng sản xuất tủ bếp Bình Thạnh</h2>
            <p>Nằm trên trục đường Bình Quới, xưởng mộc Quốc Phan có vị trí giao thông vô cùng thuận tiện, nhanh chóng tiếp cận khảo sát mặt bằng và đo đạc tại các quận trung tâm như Quận 1, Quận 2 (TP Thủ Đức), Phú Nhuận và Gò Vấp. Khách hàng có thể dễ dàng ghé thăm xưởng để duyệt trực tiếp mẫu cánh Acrylic không đường line hoặc màu vân gỗ Melamine thực tế trước khi chốt bản vẽ kỹ thuật.</p>

            <!-- <image src="" alt="Xưởng sản xuất tủ bếp Bình Thạnh với vị trí thuận lợi – Quốc Phan Design" /> -->

            <h2 id="sec-2">2. Các dòng chất liệu tủ bếp được ưa chuộng nhất 2024</h2>
            <p>Để đảm bảo độ bền tối ưu trong môi trường nấu nướng ẩm nhiệt cao, xưởng Quốc Phan chuyên gia công các giải pháp vật liệu cao cấp:</p>
            <ul>
                <li><strong>Thùng tủ bếp MDF lõi xanh chống ẩm:</strong> Độ kháng ẩm vượt trội, phủ Melamine đồng màu chống bám dầu mỡ.</li>
                <li><strong>Khoang chậu rửa bằng nhựa Picomat (PVC Foam):</strong> Chống nước 100%, vĩnh viễn không lo rò rỉ nước từ vòi hay bồn rửa làm mục ván.</li>
                <li><strong>Cánh phủ Acrylic bóng gương An Cường:</strong> Tạo cảm giác mở rộng không gian phòng bếp, bề mặt sáng bóng dễ dàng lau chùi.</li>
                <li><strong>Cánh phủ Laminate chống trầy xước:</strong> Dành cho các gia chủ yêu thích phong cách vân gỗ ấm áp, chống va quẹt hiệu quả.</li>
            </ul>

            <!-- <image src="" alt="Mẫu tủ bếp chữ L hiện đại cánh Acrylic kết hợp khoang kệ rượu tại Bình Thạnh" /> -->

            <h2 id="sec-3">3. Bố trí tam giác công năng bếp chuẩn khoa học</h2>
            <p>Một bộ tủ bếp đẹp chưa đủ, nó phải tiện dụng cho người nội trợ. Kiến trúc sư Quốc Phan luôn tuân thủ nguyên tắc <em>Tam Giác Hoạt Động (Tủ lạnh - Bồn rửa - Bếp nấu)</em> với khoảng cách di chuyển từ 1.2m đến 2.7m, giúp giảm thiểu tối đa bước chân khi chuẩn bị bữa ăn.</p>

            <!-- <image src="" alt="Hệ phụ kiện inox thông minh giá nâng hạ bát đĩa và kệ xoong nồi tủ bếp" /> -->

            <h2 id="sec-4">4. Quy trình đóng tủ bếp tại xưởng Quốc Phan</h2>
            <p>Từ lúc tiếp nhận nhu cầu đến khi hoàn thiện chỉ kéo dài từ 7 đến 10 ngày làm việc. Sản phẩm được lắp ráp thử nghiệm tại xưởng trước khi đóng kiện bọc mút xốp chuyển đến căn hộ, đảm bảo thi công lắp đặt tại nhà khách hàng chỉ mất từ 1 đến 2 ngày mà không gây bụi bặm hay tiếng ồn kéo dài.</p>
        """
    },
    {
        "id": 3,
        "slug": "bi-quyet-thiet-ke-noi-that-can-ho-3-phong-ngu.html",
        "title": "Bí Quyết Thiết Kế Nội Thất Căn Hộ 3 Phòng Ngủ – Tiện Nghi & Cân Bằng Không Gian",
        "category": "Căn Hộ Chung Cư",
        "date": "25/11/2023",
        "iso_date": "2023-11-25",
        "read_time": "7 phút đọc",
        "edition": "Số 03 • Thiết Kế Căn Hộ Gia Đình",
        "meta_desc": "Khám phá bí quyết thiết kế nội thất căn hộ 3 phòng ngủ đẹp, hiện đại. Giải pháp phân chia không gian sinh hoạt chung và phòng ngủ master, phòng trẻ em khoa học.",
        "keywords": "thiết kế căn hộ 3 phòng ngủ, nội thất chung cư 3pn, thiết kế phòng ngủ master, mẫu căn hộ 3 phòng ngủ đẹp",
        "lead": "Căn hộ 3 phòng ngủ là tổ ấm lý tưởng cho gia đình nhiều thế hệ. Bí quyết tạo nên không gian sống hoàn hảo nằm ở sự cân bằng giữa khu vực sinh hoạt chung ấm cúng và sự riêng tư tuyệt đối cho từng thành viên.",
        "toc": [
            ("sec-1", "1. Tại sao thiết kế căn hộ 3 phòng ngủ lại cần sự tính toán kỹ lưỡng?"),
            ("sec-2", "2. Thiết kế phòng khách & bếp mở tạo không gian sinh hoạt chung"),
            ("sec-3", "3. Bố trí 3 phòng ngủ: Master sang trọng, phòng ngủ con năng động"),
            ("sec-4", "4. Kinh nghiệm lựa chọn vật liệu và dự toán chi phí")
        ],
        "content_html": """
            <p>Căn hộ 3 phòng ngủ thường có diện tích từ 85m² đến 120m², là không gian sinh sống của gia đình từ 4 đến 6 thành viên. Thách thức lớn nhất của các gia chủ khi nhận bàn giao thô hoặc hoàn thiện cơ bản từ chủ đầu tư là làm sao bố trí đồ đạc đồng bộ, không bị rối mắt và tận dụng tối đa ánh sáng tự nhiên.</p>

            <h2 id="sec-1">1. Tại sao thiết kế căn hộ 3 phòng ngủ lại cần sự tính toán kỹ lưỡng?</h2>
            <p>Khác với căn hộ độc thân hay 1-2 phòng ngủ, căn hộ 3PN đòi hỏi sự hài hòa giữa nhiều độ tuổi: ông bà cần sự yên tĩnh thoáng đãng, bố mẹ cần không gian thư giãn sang trọng và con cái cần góc học tập sáng tạo, an toàn. Một bản thiết kế nội thất bài bản sẽ giúp phân luồng giao thông thông suốt, không gian không bị ngột ngạt dù chứa nhiều đồ đạc sinh hoạt.</p>

            <!-- <image src="" alt="Phối cảnh phòng khách liền bếp căn hộ 3 phòng ngủ hiện đại – Quốc Phan Design" /> -->

            <h2 id="sec-2">2. Thiết kế phòng khách & bếp mở tạo không gian sinh hoạt chung</h2>
            <p>Xu hướng không gian mở (Open Concept) kết nối liên hoàn giữa phòng khách, bàn ăn và đảo bếp đang là lựa chọn số một. Sử dụng hệ sofa chữ L bọc nỉ cao cấp cùng bàn trà mặt đá phiến, kết hợp đèn thả trần nghệ thuật tạo điểm nhấn trung tâm sang trọng.</p>

            <!-- <image src="" alt="Không gian phòng ngủ Master rộng rãi với hệ tủ quần áo cánh kính sang trọng" /> -->

            <h2 id="sec-3">3. Bố trí 3 phòng ngủ: Master sang trọng, phòng ngủ con năng động</h2>
            <p><strong>Phòng ngủ Master:</strong> Là chốn riêng tư của gia chủ, ưu tiên sử dụng giường ngủ bọc nệm đầu giường, vách ốp gỗ trang trí đầu giường tích hợp dải đèn LED âm trần 3000K dịu nhẹ, hệ tủ quần áo kịch trần kết hợp bàn trang điểm treo tường.</p>
            <p><strong>Phòng ngủ cho bé:</strong> Tùy theo bé trai hay bé gái, màu sắc sẽ được lựa chọn tươi sáng (xanh mint, pastel, vàng nhạt) kết hợp bàn học liền giá sách thông minh và giường tầng hoặc giường đơn có ngăn kéo chứa đồ chơi.</p>
            <p><strong>Phòng ngủ phụ / Phòng cho ông bà hoặc khách:</strong> Tone màu trung tính nhã nhặn, chú trọng sự êm ái của đệm ngủ và ánh sáng tự nhiên lưu thông tốt.</p>

            <!-- <image src="" alt="Mẫu phòng ngủ đôi cho bé tiện nghi với giường tầng thông minh tiết kiệm diện tích" /> -->
        """
    },
    {
        "id": 4,
        "slug": "noi-that-hien-dai-sang-trong.html",
        "title": "Nội Thất Hiện Đại Sang Trọng – Đẳng Cấp Không Gian Sống Modern Luxury",
        "category": "Xu Hướng",
        "date": "28/11/2023",
        "iso_date": "2023-11-28",
        "read_time": "5 phút đọc",
        "edition": "Số 04 • Xu Hướng Thiết Kế",
        "meta_desc": "Khám phá phong cách nội thất hiện đại sang trọng Modern Luxury: sự hòa quyện giữa vân gỗ tự nhiên, kim loại mạ vàng PVD, đá cẩm thạch và ánh sáng tinh tế.",
        "keywords": "nội thất hiện đại sang trọng, phong cách modern luxury, thiết kế nội thất sang trọng, nội thất cao cấp hcm",
        "lead": "Modern Luxury là tuyên ngôn về sự xa xỉ thầm kín (Quiet Luxury). Không phô trương cầu kỳ, phong cách này cuốn hút bởi sự trau chuốt của chất liệu thượng hạng và đường nét kiến trúc tinh gọn.",
        "toc": [
            ("sec-1", "1. Định nghĩa phong cách Modern Luxury trong kiến trúc nội thất"),
            ("sec-2", "2. Bảng màu kinh điển: Gỗ nâu trầm hòa quyện cùng tone kem & xám"),
            ("sec-3", "3. Vật liệu tạo nên đẳng cấp: Đá cẩm thạch, da bò thật và nẹp đồng PVD"),
            ("sec-4", "4. Giải đáp những câu hỏi thường gặp khi thi công nội thất cao cấp")
        ],
        "content_html": """
            <p>Phong cách nội thất <strong>Modern Luxury</strong> ra đời từ sự giao thoa hoàn mỹ giữa nét tinh giản của thiết kế đương đại và sự tráng lệ của các vật liệu cao cấp. Đây là lựa chọn hàng đầu của các chủ nhân penthouse, biệt thự và căn hộ hạng sang tại TP.HCM.</p>

            <h2 id="sec-1">1. Định nghĩa phong cách Modern Luxury trong kiến trúc nội thất</h2>
            <p>Khác biệt lớn nhất của phong cách này là sự đề cao tính cá nhân hóa và công năng ứng dụng tối ưu. Từng món đồ may đo không chỉ là đồ nội thất mà còn là một tác phẩm nghệ thuật có tỉ lệ chuẩn mực, vừa vặn tuyệt đối với không gian sống.</p>

            <!-- <image src="" alt="Không gian phòng khách phong cách Modern Luxury tone gỗ óc chó kết hợp da kem sang trọng" /> -->

            <h2 id="sec-2">2. Bảng màu kinh điển: Gỗ nâu trầm hòa quyện cùng tone kem & xám</h2>
            <p>Sự phối hợp màu sắc trong nội thất hiện đại sang trọng luôn tuân thủ nguyên tắc 60 - 30 - 10:</p>
            <ul>
                <li><strong>60% Màu chủ đạo:</strong> Trắng sứ, be, xám ghi nhạt trên tường và trần thạch cao.</li>
                <li><strong>30% Màu đồ gỗ:</strong> Gỗ óc chó (Walnut), sồi hun khói tạo chiều sâu ấm áp cho hệ tủ kệ.</li>
                <li><strong>10% Màu điểm nhấn kim loại & đá:</strong> Nẹp kim loại vàng champagne, mặt bàn đá vân mây cẩm thạch.</li>
            </ul>

            <!-- <image src="" alt="Chi tiết vách tivi ốp đá đối vân kết hợp nan gỗ và chỉ viền mạ vàng PVD" /> -->

            <h2 id="sec-3">3. Vật liệu tạo nên đẳng cấp: Đá cẩm thạch, da bò thật và nẹp đồng PVD</h2>
            <p>Chất liệu chính là linh hồn của sự sang trọng. Quốc Phan Design tuyển chọn kỹ lưỡng các dòng ván gỗ công nghiệp phủ Veneer óc chó tự nhiên nhập khẩu Bắc Mỹ, kết hợp ray trượt đóng êm Blum Movento và phụ kiện tủ áo Hafele Đức để mang đến trải nghiệm chạm êm ái nhất cho gia chủ.</p>
        """
    },
    {
        "id": 5,
        "slug": "mau-thiet-ke-noi-that-chung-cu-70m2.html",
        "title": "Mẫu Thiết Kế Nội Thất Chung Cư 70m2 – 2 Phòng Ngủ Đẹp & Tối Ưu Từng Mét Vuông",
        "category": "Căn Hộ Chung Cư",
        "date": "02/12/2023",
        "iso_date": "2023-12-02",
        "read_time": "6 phút đọc",
        "edition": "Số 05 • Giải Pháp Căn Hộ Vừa & Nhỏ",
        "meta_desc": "Tổng hợp mẫu thiết kế nội thất chung cư 70m2 với 2 phòng ngủ thông minh, hiện đại. Giải pháp bố trí nội thất kịch trần, mở rộng thị giác và tiết kiệm chi phí.",
        "keywords": "thiết kế nội thất chung cư 70m2, căn hộ 70m2 2 phòng ngủ, mẫu nội thất chung cư 70m2, chi phí làm nội thất căn hộ 70m2",
        "lead": "Diện tích 70m2 là căn hộ 2 phòng ngủ phổ biến nhất hiện nay. Chỉ cần một phương án bố trí nội thất thông minh, bạn sẽ biến 70m2 thành không gian sống rộng thoáng tựa như căn hộ 90m2.",
        "toc": [
            ("sec-1", "1. Thách thức không gian trong căn hộ chung cư 70m2"),
            ("sec-2", "2. Bố trí ánh sáng tự nhiên và mở rộng tầm nhìn"),
            ("sec-3", "3. Đồ nội thất đa năng giải phóng mặt sàn"),
            ("sec-4", "4. Dự toán chi phí thi công nội thất căn hộ 70m2 tại xưởng")
        ],
        "content_html": """
            <p>Căn hộ 70m² thường có cấu trúc: 1 phòng khách liền bếp, 2 phòng ngủ và 2 phòng vệ sinh. Để không gian luôn gọn gàng và thoáng mát, nguyên tắc vàng là <em>"tận dụng chiều cao thay vì chiếm dụng mặt sàn"</em>.</p>

            <h2 id="sec-1">1. Thách thức không gian trong căn hộ chung cư 70m2</h2>
            <p>Nếu mua sẵn đồ nội thất bán rời ngoài showroom, bạn sẽ dễ gặp tình trạng kích thước tủ quá lớn làm che khuất lối đi, hoặc tủ quá nhỏ để lộ khoảng hở đóng bụi bẩn trên nóc tủ. May đo nội thất kịch trần theo đúng kích thước hiện trạng thực tế là giải pháp triệt để nhất cho căn hộ 70m2.</p>

            <!-- <image src="" alt="Mẫu thiết kế phòng khách căn hộ chung cư 70m2 hiện đại với sofa nỉ nhỏ gọn" /> -->

            <h2 id="sec-2">2. Bố trí ánh sáng tự nhiên và mở rộng tầm nhìn</h2>
            <p>Ánh sáng tự nhiên từ ban công và cửa sổ phòng ngủ là tài sản quý giá nhất. Quốc Phan áp dụng hệ rèm 2 lớp (1 lớp voan trắng lấy sáng dịu, 1 lớp cản sáng chống nóng) kết hợp gương dán tường trang trí cạnh bàn ăn giúp phản chiếu ánh sáng và nhân đôi cảm giác chiều sâu cho gian phòng khách.</p>

            <!-- <image src="" alt="Phối cảnh ánh sáng tự nhiên tràn ngập góc làm việc trong căn hộ 70m2" /> -->

            <h2 id="sec-3">3. Đồ nội thất đa năng giải phóng mặt sàn</h2>
            <p>Hệ tủ giày liền kệ trang trí vách ngăn lối vào, giường ngủ bục tích hợp ngăn kéo đựng chăn ga gối đệm, bàn ăn thông minh có thể gấp gọn kéo dài là những món đồ không thể thiếu giúp căn hộ 70m² luôn ngăn nắp.</p>
        """
    },
    {
        "id": 6,
        "slug": "luu-y-quan-trong-khi-thi-cong-nha-pho.html",
        "title": "Những Lưu Ý Quan Trọng Khi Thi Công Nhà Phố 2023 – Tránh Phát Sinh & Đảm Bảo Tiến Độ",
        "category": "Kinh Nghiệm Thi Công",
        "date": "05/12/2023",
        "iso_date": "2023-12-05",
        "read_time": "7 phút đọc",
        "edition": "Số 06 • Cẩm Nang Xây Dựng & Hoàn Thiện",
        "meta_desc": "Tổng hợp những lưu ý sống còn khi thi công nội thất nhà phố: lựa chọn nhà thầu uy tín, kiểm tra hiện trạng tường ẩm, đi đường điện nước ngầm và kiểm soát hợp đồng.",
        "keywords": "thi công nội thất nhà phố, kinh nghiệm làm nội thất nhà phố, lưu ý hoàn thiện nhà phố, thi công nhà phố tphcm",
        "lead": "Thi công nội thất nhà phố phức tạp hơn căn hộ chung cư rất nhiều bởi kết cấu nhiều tầng, cầu thang di chuyển hẹp và độ ẩm nền móng. Dưới đây là những kinh nghiệm xương máu gia chủ cần nắm rõ.",
        "toc": [
            ("sec-1", "1. Chọn đúng đối tác: Có xưởng sản xuất trực tiếp và pháp lý rõ ràng"),
            ("sec-2", "2. Đánh giá kinh nghiệm và công trình thực tế đã thi công"),
            ("sec-3", "3. Khảo sát kỹ hiện trạng chống thấm tầng trệt và tường bao"),
            ("sec-4", "4. Kiểm soát hợp đồng bóc tách chi tiết tránh phát sinh chi phí")
        ],
        "content_html": """
            <p>Nhà phố tại các đô thị lớn như TP.HCM thường có đặc thù mặt tiền hẹp (3m - 5m) và chiều sâu kéo dài dạng ống. Khi bước vào giai đoạn hoàn thiện nội thất, nếu không có kế hoạch chi tiết từ đầu, gia chủ rất dễ rơi vào tình trạng phát sinh chi phí hàng chục triệu đồng và trễ tiến độ vào nhà mới.</p>

            <h2 id="sec-1">1. Chọn đúng đối tác: Có xưởng sản xuất trực tiếp và pháp lý rõ ràng</h2>
            <p>Thay vì thuê các công ty môi giới thiết kế nhận thầu rồi bắn lại cho các xưởng nhỏ lẻ bên ngoài, bạn nên làm việc trực tiếp với đơn vị có pháp nhân công ty rõ ràng và sở hữu xưởng mộc riêng. Điều này giúp kiểm soát chất lượng đầu vào của gỗ, đồng bộ từ khâu bản vẽ thiết kế đến khi lắp ráp đồ nội thất.</p>

            <!-- <image src="" alt="Thi công nội thất phòng khách nhà phố hiện đại với vách ốp lam sóng kết hợp đá tự nhiên" /> -->

            <h2 id="sec-2">2. Đánh giá kinh nghiệm và công trình thực tế đã thi công</h2>
            <p>Hãy yêu cầu đơn vị thi công cho bạn xem hình ảnh chụp thực tế tại các công trình nhà phố họ vừa bàn giao. Quan sát kỹ các mối ghép nối chân len tường, nẹp dán cạnh tủ áo, bản lề cửa và độ khít của các cánh tủ để đánh giá tay nghề của thợ.</p>

            <!-- <image src="" alt="Đội ngũ kỹ thuật Quốc Phan đo đạc và khảo sát hiện trạng nhà phố nhiều tầng" /> -->

            <h2 id="sec-3">3. Khảo sát kỹ hiện trạng chống thấm tầng trệt và tường bao</h2>
            <p>Khu vực tầng trệt nhà phố thường xuyên chịu tác động ẩm từ đất nền bốc lên. Đối với tủ bếp tầng trệt hoặc tủ giầy đặt sát cửa ra vào, xưởng Quốc Phan khuyến nghị sử dụng cốt gỗ nhựa Picomat chịu nước hoặc đóng chân inox cách ẩm, không đặt ván gỗ trực tiếp chạm sàn gạch ẩm ướt.</p>
        """
    },
    {
        "id": 7,
        "slug": "bao-gia-thiet-ke-noi-that-tron-goi.html",
        "title": "Báo Giá Thiết Kế Thi Công Nội Thất Trọn Gói 2023 – Chi Tiết Giá Gốc Tại Xưởng",
        "category": "Báo Giá",
        "date": "10/12/2023",
        "iso_date": "2023-12-10",
        "read_time": "6 phút đọc",
        "edition": "Số 07 • Cẩm Nang Dự Toán Chi Phí",
        "meta_desc": "Bảng báo giá thiết kế thi công nội thất trọn gói mới nhất 2023 - 2024. Đơn giá minh bạch theo mét dài tủ bếp, m2 tủ áo, gói hoàn thiện căn hộ 1PN, 2PN, 3PN.",
        "keywords": "báo giá thiết kế nội thất trọn gói, chi phí thi công nội thất, đơn giá tủ bếp mét dài, giá làm nội thất chung cư",
        "lead": "Hiểu rõ đơn giá và cách tính chi phí giúp gia chủ chủ động tài chính, không lo bị đội vốn khi hoàn thiện tổ ấm mới. Quốc Phan Design công khai bảng dự toán minh bạch chi tiết từng hạng mục.",
        "toc": [
            ("sec-1", "I. Bảng báo giá thiết kế nội thất căn hộ & nhà phố"),
            ("sec-2", "II. Đơn giá sản xuất đồ gỗ nội thất theo từng mét vuông / mét dài"),
            ("sec-3", "III. Dự toán các gói hoàn thiện căn hộ mẫu 1PN, 2PN, 3PN"),
            ("sec-4", "IV. Chính sách miễn phí 100% chi phí thiết kế khi thi công trọn gói")
        ],
        "content_html": """
            <p>Một trong những băn khoăn hàng đầu của gia chủ khi chuẩn bị làm nhà là chi phí. Tại Công Ty TNHH Thiết Kế Quốc Phan, toàn bộ đơn giá được lập dựa trên khối lượng thực tế và định mức vật tư tiêu chuẩn, hoàn toàn minh bạch không có chi phí ẩn.</p>

            <h2 id="sec-1">I. Bảng báo giá thiết kế nội thất căn hộ & nhà phố</h2>
            <p>Đơn giá thiết kế kiến trúc và phối cảnh 3D nội thất được tính theo diện tích sàn (m²):</p>
            <ul>
                <li><strong>Gói thiết kế căn hộ chung cư hiện đại:</strong> 150.000đ – 180.000đ / m².</li>
                <li><strong>Gói thiết kế nhà phố / Biệt thự:</strong> 200.000đ – 250.000đ / m².</li>
                <li><strong>Đặc biệt:</strong> Giảm ngay 50% đến 100% phí thiết kế khi ký hợp đồng thi công sản xuất nội thất trọn gói tại xưởng Quốc Phan.</li>
            </ul>

            <!-- <image src="" alt="Bảng dự toán bóc tách khối lượng chi tiết từng phòng tại xưởng Quốc Phan" /> -->

            <h2 id="sec-2">II. Đơn giá sản xuất đồ gỗ nội thất theo từng mét vuông / mét dài</h2>
            <p>Đồ gỗ may đo trực tiếp được tính theo quy chuẩn kỹ thuật ngành mộc:</p>
            <ul>
                <li><strong>Tủ bếp dưới (MDF lõi xanh chống ẩm):</strong> 2.400.000đ – 2.800.000đ / mét dài.</li>
                <li><strong>Tủ bếp trên kịch trần (MDF lõi xanh phủ Melamine):</strong> 2.200.000đ – 2.600.000đ / mét dài.</li>
                <li><strong>Cánh phủ Acrylic bóng gương noline:</strong> 3.200.000đ – 3.800.000đ / mét dài.</li>
                <li><strong>Tủ quần áo cánh lùa / cánh mở kịch trần:</strong> 2.200.000đ – 2.700.000đ / m² mặt đứng.</li>
                <li><strong>Giường ngủ 1.8m x 2.0m có ngăn kéo:</strong> 6.500.000đ – 8.500.000đ / bộ.</li>
            </ul>

            <!-- <image src="" alt="Thi công hoàn thiện căn hộ 2 phòng ngủ thực tế theo báo giá trọn gói" /> -->
        """
    },
    {
        "id": 8,
        "slug": "gioi-thieu-cong-ty-thiet-ke-quoc-phan.html",
        "title": "Giới Thiệu Về Công Ty Thiết Kế Quốc Phan – Hành Trình Kiến Tạo Tổ Ấm Từ 2017",
        "category": "Hồ Sơ Năng Lực",
        "date": "15/12/2023",
        "iso_date": "2023-12-15",
        "read_time": "5 phút đọc",
        "edition": "Số 08 • Câu Chuyện Thương Hiệu",
        "meta_desc": "Hành trình thành lập và phát triển của Công Ty TNHH Thiết Kế Quốc Phan từ năm 2017. Xưởng sản xuất đồ gỗ nội thất hiện đại tại 434/34 Bình Quới, Bình Thạnh, TP.HCM.",
        "keywords": "công ty tnhh thiết kế quốc phan, quoc phan design, giới thiệu quốc phan, xưởng mộc quốc phan bình thạnh",
        "lead": "Thành lập từ ngày 26/04/2017, Công Ty TNHH Thiết Kế Quốc Phan đã đồng hành cùng hàng ngàn gia đình, nhà đầu tư căn hộ và đối tác kiến trúc sư xây đắp nên những không gian sống bền đẹp, tinh tế.",
        "toc": [
            ("sec-1", "1. Lịch sử hình thành và phát triển thương hiệu"),
            ("sec-2", "2. Triết lý kinh doanh: Làm việc bằng cái tâm và chuẩn mực tay nghề"),
            ("sec-3", "3. Năng lực xưởng sản xuất máy móc CNC tự động hóa"),
            ("sec-4", "4. Thông tin doanh nghiệp và địa chỉ liên hệ chính thức")
        ],
        "content_html": """
            <p><strong>Công Ty TNHH Thiết Kế Quốc Phan</strong> (MST: 0314372672) được cấp phép hoạt động từ ngày 26/04/2017. Trải qua gần một thập kỷ xây dựng và trưởng thành, chúng tôi tự hào là đơn vị khép kín từ khâu tư vấn thiết kế kiến trúc, sản xuất gia công đồ gỗ tại xưởng cho đến thi công hoàn thiện chìa khóa trao tay.</p>

            <h2 id="sec-1">1. Lịch sử hình thành và phát triển thương hiệu</h2>
            <p>Bắt đầu từ một xưởng mộc truyền thống với niềm đam mê sâu sắc với từng thớ gỗ, Quốc Phan đã không ngừng nâng cấp đầu tư trang thiết bị công nghệ hiện đại. Ngày nay, chúng tôi phục vụ hàng trăm dự án mỗi năm từ các căn hộ cao cấp như Vinhomes Central Park, Hà Đô Centrosa, Saigon South Residences đến các biệt thự, nhà phố tại Bình Thạnh, Gò Vấp, Quận 2 và Quận 7.</p>

            <!-- <image src="" alt="Đội ngũ kiến trúc sư và thợ mộc lành nghề tại xưởng sản xuất Quốc Phan Design" /> -->

            <h2 id="sec-2">2. Triết lý kinh doanh: Làm việc bằng cái tâm và chuẩn mực tay nghề</h2>
            <p>Chúng tôi không xem việc làm nội thất là một giao dịch thương mại đơn thuần, mà là sứ mệnh kiến tạo không gian sống tiện nghi, nuôi dưỡng hạnh phúc của mỗi gia đình. Từng mét ván cắt ra, từng đường nẹp dán đều được kiểm định khắt khe trước khi xuất xưởng.</p>

            <!-- <image src="" alt="Hệ thống máy cắt CNC và máy dán cạnh tự động tại xưởng gỗ Quốc Phan" /> -->

            <h2 id="sec-3">3. Năng lực xưởng sản xuất máy móc CNC tự động hóa</h2>
            <p>Xưởng mộc Quốc Phan tọa lạc tại 434/34 Bình Quới, Phường 28, Quận Bình Thạnh có quy mô rộng rãi, trang bị máy cắt ván tự động CNC liên kết phần mềm thiết kế 3D, máy dán cạnh nẹp tự động đa chức năng và buồng sơn cách bụi hiện đại, đảm bảo sản phẩm xuất xưởng có độ sắc nét hoàn mỹ.</p>
        """
    },
    {
        "id": 9,
        "slug": "thi-cong-noi-that-phu-my-hung-quan-7.html",
        "title": "Thi Công Nội Thất Phú Mỹ Hưng Quận 7 – Sang Trọng, Tinh Tế Chuẩn Thượng Lưu",
        "category": "Dự Án Thực Tế",
        "date": "18/12/2023",
        "iso_date": "2023-12-18",
        "read_time": "8 phút đọc",
        "edition": "Số 09 • Hồ Sơ Dự Án Tiêu Biểu",
        "meta_desc": "Dự án thi công nội thất căn hộ biệt thự Phú Mỹ Hưng Quận 7 bởi Quốc Phan Design. Phong cách sang trọng, vật liệu gỗ cao cấp, phụ kiện thông minh chuẩn thượng lưu.",
        "keywords": "thi công nội thất phú mỹ hưng quận 7, nội thất quận 7, thiết kế biệt thự phú mỹ hưng, hoàn thiện nội thất căn hộ quận 7",
        "lead": "Khu đô thị kiểu mẫu Phú Mỹ Hưng Quận 7 luôn đặt ra những tiêu chuẩn khắt khe về mặt thẩm mỹ và chất lượng thi công. Dự án do Quốc Phan đảm nhận là sự kết hợp ăn ý giữa không gian xanh và nội thất sang trọng.",
        "toc": [
            ("sec-1", "I. Những điểm nổi bật tại dự án thi công nội thất Phú Mỹ Hưng"),
            ("sec-2", "II. Giải pháp thiết kế phòng khách & đại sảnh thông tầng"),
            ("sec-3", "III. Không gian bếp đảo đẳng cấp cho các bữa tiệc gia đình"),
            ("sec-4", "IV. Phòng ngủ Master chuẩn khách sạn 5 sao quốc tế")
        ],
        "content_html": """
            <p>Phú Mỹ Hưng được mệnh danh là khu đô thị đáng sống bậc nhất Sài Gòn. Khi đảm nhận gói thầu thi công nội thất cho căn hộ cao cấp tại đây, Quốc Phan Design đã đặt ra tiêu chuẩn cao nhất về tính thẩm mỹ, sự tiện nghi và độ an toàn sức khỏe từ vật liệu gỗ đạt chuẩn phát thải E1 quốc tế.</p>

            <h2 id="sec-1">I. Những điểm nổi bật tại dự án thi công nội thất Phú Mỹ Hưng</h2>
            <p>Dự án sở hữu diện tích rộng rãi với tầm nhìn thoáng đãng ra công viên rợp bóng cây xanh. Ý tưởng chủ đạo là đưa ánh sáng tự nhiên ngập tràn vào không gian, kết hợp hệ đồ gỗ sồi tự nhiên màu sáng cùng các chi tiết bọc da bò Ý cao cấp.</p>

            <!-- <image src="" alt="Phòng khách rộng mở nhìn ra công viên tại dự án Phú Mỹ Hưng Quận 7" /> -->

            <h2 id="sec-2">II. Giải pháp thiết kế phòng khách & đại sảnh thông tầng</h2>
            <p>Khu vực phòng khách được nhấn nhá bằng hệ vách ốp kết hợp giữa gỗ tự nhiên xẻ nan nghệ thuật và đá marble cẩm thạch trắng Calacatta sang trọng. Bàn trà đôi chân kim loại mạ PVD bóng loáng mang lại vẻ đẹp quyền quý nhưng vẫn rất thanh thoát.</p>

            <!-- <image src="" alt="Hệ tủ bếp kết hợp đảo bếp bar sang trọng tại căn hộ Phú Mỹ Hưng" /> -->
        """
    },
    {
        "id": 10,
        "slug": "xuong-san-xuat-noi-that-quoc-phan.html",
        "title": "Quy Trình Hoạt Động Xưởng Sản Xuất Nội Thất Quốc Phan – Máy Móc Hiện Đại, Chuẩn Tiến Độ",
        "category": "Xưởng Sản Xuất",
        "date": "22/12/2023",
        "iso_date": "2023-12-22",
        "read_time": "5 phút đọc",
        "edition": "Số 10 • Năng Lực Sản Xuất",
        "meta_desc": "Khám phá quy trình sản xuất nội thất gỗ công nghiệp tại xưởng Quốc Phan Bình Thạnh: hệ thống hút bụi trung tâm, máy CNC cắt tự động, kho lưu trữ và đóng gói chuyên nghiệp.",
        "keywords": "xưởng sản xuất nội thất quốc phan, quy trình xưởng mộc cnc, máy dán cạnh tự động, đóng đồ gỗ theo yêu cầu hcm",
        "lead": "Sức mạnh cốt lõi của Quốc Phan Design nằm ở xưởng sản xuất quy mô bài bản. Cùng tìm hiểu quy trình khép kín từ phôi gỗ thô sơ đến thành phẩm hoàn mỹ trên dây chuyền máy móc hiện đại.",
        "toc": [
            ("sec-1", "1. Hệ thống hút bụi trung tâm bảo vệ môi trường và bề mặt ván"),
            ("sec-2", "2. Khu vực máy cắt CNC & dán cạnh nẹp tự động đa chức năng"),
            ("sec-3", "3. Buồng phun sơn phòng sạch cách ly bụi mịn"),
            ("sec-4", "4. Khu vực đóng gói, lưu trữ và bàn giao công trình")
        ],
        "content_html": """
            <p>Để đảm bảo hàng ngàn mét vuông sản phẩm nội thất xuất xưởng mỗi tháng luôn chuẩn xác tới từng milimet, <strong>Xưởng Sản Xuất Nội Thất Quốc Phan</strong> được quy hoạch thành các phân khu chuyên biệt với tiêu chuẩn 5S nghiêm ngặt.</p>

            <h2 id="sec-1">1. Hệ thống hút bụi trung tâm bảo vệ môi trường và bề mặt ván</h2>
            <p>Chúng tôi trang bị hệ thống đường ống hút bụi chân không công suất lớn nối trực tiếp tới từng đầu máy cưa, máy phay CNC. Bề mặt ván gỗ trước khi dán cạnh luôn được làm sạch tuyệt đối, ngăn ngừa tình trạng cộm phồng hay nổi bọt khí.</p>

            <!-- <image src="" alt="Hệ thống hút bụi công nghiệp và khu vực thao tác máy xưởng Quốc Phan" /> -->

            <h2 id="sec-2">2. Khu vực máy cắt CNC & dán cạnh nẹp tự động đa chức năng</h2>
            <p>Dữ liệu bản vẽ 3D được số hóa trực tiếp và chuyển sang mã G-code cho máy CNC tự động cắt, khoan lỗ cam chốt chính xác. Nhờ đó, công đoạn lắp ráp khung tủ tại công trình diễn ra ăn khớp, nhanh chóng và chuẩn xác tuyệt đối.</p>

            <!-- <image src="" alt="Kho lưu trữ vật tư gỗ An Cường và khu vực đóng gói xuất xưởng an toàn" /> -->
        """
    },
    {
        "id": 11,
        "slug": "noi-that-chung-cu-cao-cap.html",
        "title": "Nội Thất Chung Cư Cao Cấp – Xu Hướng Thiết Kế Sang Trọng, Tinh Tế Mới Nhất",
        "category": "Căn Hộ Chung Cư",
        "date": "26/12/2023",
        "iso_date": "2023-12-26",
        "read_time": "6 phút đọc",
        "edition": "Số 11 • Chuyên Đề Căn Hộ Hạng Sang",
        "meta_desc": "Thiết kế thi công nội thất chung cư cao cấp. Lựa chọn vật liệu gỗ công nghiệp cao cấp An Cường, phụ kiện ray giảm chấn, vách kính lùa thông minh tối ưu không gian.",
        "keywords": "nội thất chung cư cao cấp, thiết kế căn hộ cao cấp hcm, thi công nội thất căn hộ hạng sang, nội thất gỗ an cường",
        "lead": "Sở hữu một căn hộ chung cư cao cấp đòi hỏi phong cách nội thất tương xứng. Không chỉ đẹp ở hình thức, nội thất cao cấp còn là sự hài lòng khi chạm tay vào từng bề mặt vật liệu êm dịu.",
        "toc": [
            ("sec-1", "1. Tiêu chí đánh giá một không gian nội thất chung cư cao cấp"),
            ("sec-2", "2. Ứng dụng vách kính lùa và đèn LED chiếu điểm nghệ thuật"),
            ("sec-3", "3. Sự đồng bộ giữa nội thất rời và hệ tủ may đo cố định")
        ],
        "content_html": """
            <p>Tại các dự án chung cư cao cấp, cư dân không chỉ mua một mét vuông ở, mà là tận hưởng trải nghiệm sống tiện nghi và thư giãn sau một ngày dài làm việc. Việc thiết kế nội thất vì thế phải đặt sự thoải mái và yếu tố công thái học (Ergonomics) lên hàng đầu.</p>

            <!-- <image src="" alt="Phối cảnh phòng khách chung cư cao cấp với hệ tủ rượu cánh kính đèn LED âm tủ" /> -->

            <h2 id="sec-1">1. Tiêu chí đánh giá một không gian nội thất chung cư cao cấp</h2>
            <p>Nội thất cao cấp được nhận biết qua 3 yếu tố: sự tinh tế của các chi tiết ghép mộng, sự êm ái của toàn bộ hệ thống ray giảm chấn khi đóng mở hộc tủ, và khả năng phối trộn màu sắc hài hòa không gây mỏi mắt.</p>

            <!-- <image src="" alt="Không gian phòng ngủ master cao cấp với sàn gỗ và vách ốp nỉ ấm áp" /> -->
        """
    },
    {
        "id": 12,
        "slug": "tu-bep-binh-thanh-chat-luong-cao.html",
        "title": "Tủ Bếp Bình Thạnh Chất Lượng Cao – Giải Pháp Bề Mặt Melamine Chống Trầy Xước",
        "category": "Tủ Bếp",
        "date": "29/12/2023",
        "iso_date": "2023-12-29",
        "read_time": "5 phút đọc",
        "edition": "Số 12 • Giải Pháp Tủ Bếp Gia Đình",
        "meta_desc": "Thi công tủ bếp Bình Thạnh chất lượng cao. Thùng tủ MFC phủ Melamine chống ẩm, đa dạng vân gỗ hiện đại, phụ kiện tay nâng thông minh tiện lợi cho người nội trợ.",
        "keywords": "tủ bếp bình thạnh chất lượng cao, tủ bếp melamine bình thạnh, đóng tủ bếp gỗ mdf bình thạnh, tủ bếp đẹp giá rẻ",
        "lead": "Tủ bếp Melamine là lựa chọn cân bằng hoàn hảo giữa chi phí hợp lý và độ bền vượt trội. Tìm hiểu giải pháp thi công tủ bếp MFC lõi xanh phủ Melamine cao cấp tại xưởng Bình Thạnh.",
        "toc": [
            ("sec-1", "1. Bề mặt thùng tủ bếp Bình Thạnh MFC phủ Melamine chống ẩm"),
            ("sec-2", "2. Sự đa dạng trong màu sắc và hoa văn vân gỗ tự nhiên"),
            ("sec-3", "3. Bảng phụ kiện inox thông minh nâng tầm trải nghiệm nấu nướng")
        ],
        "content_html": """
            <p>Với ưu điểm giá thành phải chăng, bề mặt chống trầy xước tốt và bảng màu phong phú lên tới hơn 300 mã vân gỗ khác nhau, <strong>tủ bếp phủ Melamine</strong> luôn là sự lựa chọn phổ biến nhất của các hộ gia đình trẻ tại Bình Thạnh.</p>

            <h2 id="sec-1">1. Bề mặt thùng tủ bếp Bình Thạnh MFC phủ Melamine chống ẩm</h2>
            <p>Cốt gỗ ván dăm chống ẩm (MFC lõi xanh) hoặc ván sợi mật độ trung bình (MDF lõi xanh) được tẩm sấy keo chịu nước chuyên dụng, ép nóng lớp giấy phủ Melamine bảo vệ ngăn ngừa sự thẩm thấu của chất lỏng.</p>

            <!-- <image src="" alt="Mẫu tủ bếp Melamine vân gỗ sồi kết hợp cánh trắng tinh tế tại Bình Thạnh" /> -->

            <h2 id="sec-2">2. Sự đa dạng trong màu sắc và hoa văn vân gỗ tự nhiên</h2>
            <p>Từ các tone vân gỗ sồi Scandinavia sáng màu đến tone gỗ óc chó nâu trầm ấm áp, Melamine tái hiện sắc sảo từng đường vân gỗ tự nhiên mà không lo mối mọt hay co ngót theo thời gian.</p>
        """
    },
    {
        "id": 13,
        "slug": "thiet-ke-thi-cong-can-ho-ha-do-centrosa.html",
        "title": "Thiết Kế Và Thi Công Nội Thất Căn Hộ Hà Đô Centrosa – Thực Tế Trọn Gói",
        "category": "Dự Án Thực Tế",
        "date": "04/01/2024",
        "iso_date": "2024-01-04",
        "read_time": "8 phút đọc",
        "edition": "Số 13 • Dự Án Căn Hộ Trung Tâm",
        "meta_desc": "Hồ sơ thiết kế và thi công hoàn thiện nội thất căn hộ Hà Đô Centrosa Garden Quận 10 do Quốc Phan Design thực hiện: tổng quan dự án, phối cảnh 3D và bàn giao chìa khóa.",
        "keywords": "thiết kế nội thất hà đô centrosa, thi công căn hộ hà đô centrosa, nội thất chung cư hà đô quận 10, mẫu căn hộ hà đô centrosa",
        "lead": "Dự án căn hộ cao cấp Hà Đô Centrosa Garden (Quận 10) là một trong những công trình nổi bật do Quốc Phan Design thi công trọn gói, mang lại không gian sống tiện nghi vượt bậc giữa lòng thành phố.",
        "toc": [
            ("sec-1", "1. Tổng quan dự án thiết kế và thi công căn hộ Hà Đô Centrosa"),
            ("sec-2", "2. Ý tưởng thiết kế phòng khách liền ban công thoáng đãng"),
            ("sec-3", "3. Bố trí bếp chữ I gọn gàng tiện lợi"),
            ("sec-4", "4. Không gian phòng ngủ và góc làm việc tại gia")
        ],
        "content_html": """
            <p>Tọa lạc tại vị trí đắc địa số 200 đường Ba Tháng Hai, Quận 10, khu phức hợp <strong>Hà Đô Centrosa Garden</strong> sở hữu kiến trúc hiện đại chuẩn xanh. Chủ nhân căn hộ 2 phòng ngủ đã tin tưởng lựa chọn Quốc Phan Design may đo toàn bộ hệ thống đồ gỗ nội thất.</p>

            <h2 id="sec-1">1. Tổng quan dự án thiết kế và thi công căn hộ Hà Đô Centrosa</h2>
            <p>Căn hộ có diện tích 86m², hướng nhìn thông thoáng ra trung tâm Sài Gòn. Gia chủ yêu thích phong cách hiện đại ấm cúng, ưu tiên sử dụng tone màu be nhã nhặn kết hợp gỗ MDF lõi xanh chống ẩm An Cường cao cấp.</p>

            <!-- <image src="" alt="Phòng khách căn hộ Hà Đô Centrosa Quận 10 hoàn thiện thực tế – Quốc Phan Design" /> -->

            <h2 id="sec-2">2. Ý tưởng thiết kế phòng khách liền ban công thoáng đãng</h2>
            <p>Hệ tủ tivi được thiết kế treo tường tối giản kết hợp nan ốp gỗ trang trí tạo cảm giác thanh thoát. Điểm xuyết cùng sofa nỉ cao cấp và thảm dệt tay tạo nên không gian tiếp khách thân mật, sang trọng.</p>

            <!-- <image src="" alt="Hệ tủ quần áo kịch trần kết hợp bàn trang điểm phòng ngủ căn hộ Hà Đô" /> -->
        """
    },
    {
        "id": 14,
        "slug": "thi-cong-tu-bep-tphcm-uy-tin.html",
        "title": "Thi Công Tủ Bếp TPHCM Uy Tín – Báo Giá Tại Xưởng, Bảo Hành 5 Năm",
        "category": "Tủ Bếp",
        "date": "08/01/2024",
        "iso_date": "2024-01-08",
        "read_time": "6 phút đọc",
        "edition": "Số 14 • Dịch Vụ Tủ Bếp Chuyên Sâu",
        "meta_desc": "Dịch vụ thi công tủ bếp TPHCM uy tín, chất lượng từ xưởng Quốc Phan. Chuyên đóng tủ bếp Acrylic bóng gương, Melamine chống ẩm, Laminate cao cấp giao hàng đúng hẹn.",
        "keywords": "thi công tủ bếp tphcm, đóng tủ bếp tphcm, tủ bếp gỗ công nghiệp tphcm, xưởng tủ bếp uy tín hcm",
        "lead": "Tìm đơn vị thi công tủ bếp uy tín tại TP.HCM không còn là nỗi lo. Với xưởng sản xuất hiện đại và quy trình chuyên nghiệp, Quốc Phan Design cam kết mang lại sản phẩm tủ bếp may đo chuẩn từng centimet.",
        "toc": [
            ("sec-1", "1. Thực trạng thị trường tủ bếp tại TP.HCM hiện nay"),
            ("sec-2", "2. Tiêu chuẩn chống ẩm và chống cong vênh của Quốc Phan"),
            ("sec-3", "3. Bảng phụ kiện inox 304 chính hãng: Blum, Hafele, Eurogold"),
            ("sec-4", "4. Quy trình tư vấn, đo đạc và lắp ráp tận nhà")
        ],
        "content_html": """
            <p>TP.HCM với khí hậu nhiệt đới gió mùa có độ ẩm không khí cao, việc lựa chọn chất liệu đóng tủ bếp cần đặc biệt chú ý đến tính kháng ẩm và chống mối mọt. Đóng tủ bếp trực tiếp tại xưởng Quốc Phan giúp khách hàng yên tâm tuyệt đối về nguồn gốc xuất xứ vật tư.</p>

            <!-- <image src="" alt="Mẫu tủ bếp chữ U có quầy bar sang trọng thi công tại TPHCM – Quốc Phan Design" /> -->

            <h2 id="sec-1">1. Thực trạng thị trường tủ bếp tại TP.HCM hiện nay</h2>
            <p>Nhiều xưởng trôi nổi sử dụng phôi gỗ tạp kém chất lượng hoặc dán cạnh thủ công bằng bàn là khiến mép tủ nhanh chóng bị bong tróc sau vài tháng sử dụng. Quốc Phan sử dụng 100% máy dán cạnh nẹp nhiệt tự động đa chức năng với keo PUR chống nước cao cấp.</p>

            <!-- <image src="" alt="Hệ tay nâng cánh tủ bếp Blum Aventos trợ lực nhẹ nhàng thi công tại TPHCM" /> -->
        """
    },
    {
        "id": 15,
        "slug": "thiet-ke-noi-that-can-ho-2-phong-ngu.html",
        "title": "Thiết Kế Nội Thất Căn Hộ 2 Phòng Ngủ – Mẫu Căn Hộ Đẹp, Hiện Đại & Tối Ưu",
        "category": "Căn Hộ Chung Cư",
        "date": "12/01/2024",
        "iso_date": "2024-01-12",
        "read_time": "6 phút đọc",
        "edition": "Số 15 • Căn Hộ Tiêu Chuẩn",
        "meta_desc": "Mẫu thiết kế nội thất căn hộ 2 phòng ngủ đẹp ngất ngây. Giải pháp bố trí phòng khách liền bếp, tối ưu ánh sáng tự nhiên và công năng sử dụng cho gia đình trẻ.",
        "keywords": "thiết kế nội thất căn hộ 2 phòng ngủ, mẫu căn hộ 2pn đẹp, thiết kế chung cư 2 phòng ngủ, nội thất căn hộ gia đình trẻ",
        "lead": "Căn hộ 2 phòng ngủ là sự lựa chọn số 1 cho các cặp vợ chồng trẻ hoặc gia đình có 1 con. Làm sao để thiết kế vừa đẹp mắt, vừa đủ không gian chứa đồ đạc mà vẫn thoáng đãng?",
        "toc": [
            ("sec-1", "1. Bố cục mặt bằng căn hộ 2 phòng ngủ thông minh"),
            ("sec-2", "2. Chọn lựa phong cách: Scandinavian, Hiện đại hay Tối giản?"),
            ("sec-3", "3. Thiết kế phòng ngủ con linh hoạt theo độ tuổi phát triển")
        ],
        "content_html": """
            <p>Căn hộ 2 phòng ngủ thường dao động từ 55m² đến 75m². Đây là diện tích lý tưởng để kiến trúc sư thỏa sức sáng tạo các giải pháp đồ gỗ may đo đa năng, tạo nên không gian sinh hoạt ấm cúng và ngập tràn năng lượng tích cực.</p>

            <!-- <image src="" alt="Phối cảnh 3D tổng thể căn hộ 2 phòng ngủ hiện đại với gam màu pastel thanh lịch" /> -->

            <h2 id="sec-1">1. Bố cục mặt bằng căn hộ 2 phòng ngủ thông minh</h2>
            <p>Phòng khách và khu vực bàn ăn nên được đặt ở vị trí trung tâm đón ánh sáng tự nhiên từ logia. Hai phòng ngủ bố trí tách biệt về hai phía hoặc kế bên nhau với cửa mở hợp phong thủy.</p>

            <!-- <image src="" alt="Phòng ngủ phụ với giường bục thông minh kết hợp bàn học bên cửa sổ" /> -->
        """
    },
    {
        "id": 16,
        "slug": "thi-cong-noi-that-chung-cu-2-phong-ngu.html",
        "title": "Thi Công Nội Thất Chung Cư 2 Phòng Ngủ – Trọn Gói Từ Bản Vẽ Đến Bàn Giao",
        "category": "Căn Hộ Chung Cư",
        "date": "16/01/2024",
        "iso_date": "2024-01-16",
        "read_time": "7 phút đọc",
        "edition": "Số 16 • Thực Tế Công Trình",
        "meta_desc": "Hồ sơ thực tế thi công nội thất chung cư 2 phòng ngủ tại TPHCM: tiến độ sản xuất tại xưởng 10 ngày, lắp đặt 2 ngày, hình ảnh thực tế bàn giao sắc nét từng góc cạnh.",
        "keywords": "thi công nội thất chung cư 2 phòng ngủ, hoàn thiện căn hộ 2pn, thi công đồ gỗ căn hộ 2 phòng ngủ, nội thất trọn gói tphcm",
        "lead": "Hình ảnh thực tế thi công luôn là thước đo chân thực nhất cho năng lực xưởng sản xuất. Cùng ngắm nhìn bộ ảnh bàn giao căn hộ 2 phòng ngủ hoàn thiện thực tế từ Quốc Phan Design.",
        "toc": [
            ("sec-1", "1. Nhật ký công trình: Khảo sát hiện trạng & lắp đặt"),
            ("sec-2", "2. Chiêm ngưỡng không gian hoàn thiện thực tế"),
            ("sec-3", "3. Đánh giá chất lượng đường dán cạnh và phụ kiện tủ")
        ],
        "content_html": """
            <p>Biến một bản vẽ phối cảnh 3D đẹp lung linh thành sản phẩm thật ngoài đời thực mà không có sự chênh lệch là cam kết hàng đầu của Quốc Phan. Mỗi công trình căn hộ 2 phòng ngủ đều được chúng tôi quản lý tiến độ chặt chẽ qua từng mốc nghiệm thu.</p>

            <!-- <image src="" alt="Hình ảnh thực tế bàn giao phòng khách căn hộ 2 phòng ngủ sạch sẽ, sắc nét" /> -->

            <h2 id="sec-1">1. Nhật ký công trình: Khảo sát hiện trạng & lắp đặt</h2>
            <p>Từ lúc tiếp nhận bàn giao thô từ chủ đầu tư, đội ngũ kỹ thuật Quốc Phan tiến hành quét laser kiểm tra độ thẳng của tường và góc vuông của các góc chết, đảm bảo khi đưa tủ áo kịch trần vào lắp ráp không bị hở khe tường.</p>

            <!-- <image src="" alt="Góc tủ bếp và bàn ăn hoàn thiện thực tế chuẩn xác 100% so với bản vẽ 3D" /> -->
        """
    },
    {
        "id": 17,
        "slug": "thiet-ke-thi-cong-phong-ngu-dep.html",
        "title": "Thiết Kế Thi Công Phòng Ngủ Đẹp 2023 – Không Gian Nghỉ Ngơi Ấm Cúng, Tiện Nghi",
        "category": "Phòng Ngủ",
        "date": "20/01/2024",
        "iso_date": "2024-01-20",
        "read_time": "5 phút đọc",
        "edition": "Số 17 • Không Gian Phòng Ngủ",
        "meta_desc": "Thiết kế thi công phòng ngủ đẹp hiện đại 2023. Các mẫu giường ngủ may đo thông minh, tủ áo cánh kính thời thượng, vách ốp đầu giường ấm áp hợp phong thủy.",
        "keywords": "thiết kế thi công phòng ngủ đẹp, mẫu phòng ngủ hiện đại, giường ngủ may đo, tủ quần áo phòng ngủ hcm",
        "lead": "Phòng ngủ là nơi tái tạo năng lượng sau một ngày làm việc bận rộn. Một thiết kế phòng ngủ đẹp cần mang lại cảm giác bình yên, êm dịu và tiện nghi cho giấc ngủ sâu.",
        "toc": [
            ("sec-1", "1. Tổng quan dự án thiết kế thi công phòng ngủ 2023"),
            ("sec-2", "2. Hình ảnh thực tế khi thi công phòng ngủ may đo"),
            ("sec-3", "3. Lựa chọn ánh sáng và màu sắc hợp phong thủy bản mệnh")
        ],
        "content_html": """
            <p>Trong thiết kế nội thất phòng ngủ, sự êm ái và tiện dụng luôn được đặt lên hàng đầu. Đồ gỗ may đo như giường ngủ, tab đầu giường và tủ quần áo cần có kích thước đồng bộ, tạo nên một tổng thể liền mạch, thư thái.</p>

            <h2 id="sec-1">1. Tổng quan dự án thiết kế thi công phòng ngủ 2023</h2>
            <p>Dự án phòng ngủ master được KTS Quốc Phan thiết kế theo phong cách hiện đại với gam màu nâu gỗ kết hợp be sáng. Giường ngủ bọc đệm êm ái kết hợp vách ốp gỗ trang trí tích hợp đèn LED hắt khe tường tạo không gian lãng mạn.</p>

            <!-- <image src="" alt="Mẫu phòng ngủ master với hệ vách ốp đầu giường gỗ kết hợp nẹp chỉ kim loại sang trọng" /> -->

            <h2 id="sec-2">2. Hình ảnh thực tế khi thi công phòng ngủ may đo</h2>
            <p>Tủ áo kịch trần kết hợp bàn trang điểm được đo đạc tỉ mỉ theo đúng chiều cao trần nhà, loại bỏ hoàn toàn góc chết đóng bụi và nhân đôi khả năng chứa đồ cho gia chủ.</p>

            <!-- <image src="" alt="Chi tiết tủ quần áo cánh kính viền nhôm xingfa anode cao cấp tại phòng ngủ" /> -->
        """
    },
    {
        "id": 18,
        "slug": "thi-cong-noi-that-chung-cu-ssg-tower.html",
        "title": "Thi Công Nội Thất Chung Cư SSG Tower 2023 – Hoàn Thiện Căn Hộ Cao Cấp",
        "category": "Dự Án Thực Tế",
        "date": "24/01/2024",
        "iso_date": "2024-01-24",
        "read_time": "7 phút đọc",
        "edition": "Số 18 • Dự Án Biểu Tượng",
        "meta_desc": "Dự án thi công nội thất căn hộ chung cư SSG Tower (Opal Saigon Pearl / SSR) năm 2023. May đo đồ gỗ chống ẩm cao cấp, đường nét tinh xảo đẳng cấp 5 sao.",
        "keywords": "thi công nội thất chung cư ssg, nội thất căn hộ ssg tower, thi công căn hộ opal saigon pearl, nội thất cao cấp bình thạnh",
        "lead": "Tòa tháp SSG Tower là biểu tượng căn hộ cao cấp tại cửa ngõ Bình Thạnh. Dự án hoàn thiện nội thất do Quốc Phan thi công khẳng định tay nghề xuất sắc của đội ngũ thợ mộc xưởng nhà.",
        "toc": [
            ("sec-1", "1. Tổng quan dự án thi công nội thất chung cư SSG"),
            ("sec-2", "2. Giải pháp nội thất phòng khách liên thông phòng ăn"),
            ("sec-3", "3. Phòng ngủ view sông Sài Gòn thoáng đãng")
        ],
        "content_html": """
            <p>Căn hộ tại dự án SSG Tower sở hữu tầm nhìn đắt giá ôm trọn bán đảo Thanh Đa và sông Sài Gòn thơ mộng. Để tôn vinh tầm nhìn tuyệt mỹ này, nội thất được thiết kế tinh giản tối đa với những đường nét thanh mảnh, tránh cảm giác cồng kềnh che khuất cửa sổ kính kịch sàn.</p>

            <!-- <image src="" alt="Không gian phòng khách căn hộ chung cư SSG Tower view sông Sài Gòn thoáng mát" /> -->

            <h2 id="sec-1">1. Tổng quan dự án thi công nội thất chung cư SSG</h2>
            <p>Căn hộ có diện tích 115m² với 3 phòng ngủ tiện nghi. Toàn bộ vách ốp trang trí và hệ tủ áo được may đo bằng cốt ván HDF siêu chống ẩm phủ Veneer sồi tự nhiên sơn bóng mờ PU cao cấp.</p>

            <!-- <image src="" alt="Chi tiết bàn ăn nguyên tấm kết hợp ghế ăn bọc da cao cấp tại căn hộ SSG" /> -->
        """
    },
    {
        "id": 19,
        "slug": "tong-hop-mau-noi-that-dep-xu-huong-moi.html",
        "title": "Mẫu Nội Thất Đẹp 2024 – Bộ Sưu Tập Thiết Kế Đón Đầu Xu Hướng Mới",
        "category": "Xu Hướng",
        "date": "28/01/2024",
        "iso_date": "2024-01-28",
        "read_time": "6 phút đọc",
        "edition": "Số 19 • Bộ Sưu Tập Xu Hướng",
        "meta_desc": "Tổng hợp các mẫu nội thất đẹp 2024: phòng khách sang trọng, nhà bếp hiện đại, phòng ngủ ấm áp. Cập nhật xu hướng vật liệu sinh thái và công nghệ nhà thông minh.",
        "keywords": "mẫu nội thất đẹp 2024, xu hướng thiết kế nội thất mới, mẫu phòng khách đẹp 2024, mẫu phòng bếp đẹp",
        "lead": "Năm 2024 đánh dấu sự lên ngôi của lối sống xanh, vật liệu bền vững và nội thất thông minh tiện nghi. Khám phá những mẫu thiết kế dẫn đầu xu hướng được khách hàng săn đón nhất.",
        "toc": [
            ("sec-1", "I. Xu hướng nội thất phòng khách hiện đại 2024"),
            ("sec-2", "II. Nội thất nhà bếp đẹp & tiện nghi 2024"),
            ("sec-3", "III. Không gian phòng ngủ thư thái hướng về thiên nhiên")
        ],
        "content_html": """
            <p>Bước sang năm 2024, xu hướng thiết kế nội thất hướng mạnh về tính cá nhân hóa, chú trọng vật liệu thân thiện với sức khỏe và đề cao sự thư giãn tinh thần (Wellness Living). Nhà không chỉ là nơi che mưa nắng, mà là chốn chữa lành và nạp lại năng lượng sống.</p>

            <h2 id="sec-1">I. Xu hướng nội thất phòng khách hiện đại 2024</h2>
            <p>Các đường bo cong mềm mại (Curved furniture) trên sofa, bàn trà và hệ vách ngăn đang thay thế dần các góc vuông sắc nhọn thô cứng, mang lại cảm giác ấm cúng, an toàn và uyển chuyển cho gian phòng khách.</p>

            <!-- <image src="" alt="Mẫu nội thất phòng khách đẹp 2024 với đường nét bo cong mềm mại và cây xanh" /> -->

            <h2 id="sec-2">II. Nội thất nhà bếp đẹp & tiện nghi 2024</h2>
            <p>Nhà bếp năm 2024 tôn vinh sự tối giản sạch sẽ với hệ cánh tủ phẳng không tay nắm (J-pull / Gola nhôm), kết hợp máy rửa chén âm tủ và bồn chậu rửa đúc liền khối thẩm mỹ cao.</p>

            <!-- <image src="" alt="Mẫu nhà bếp đẹp 2024 với hệ tủ phẳng không tay nắm kết hợp ánh sáng LED thanh ray" /> -->
        """
    },
    {
        "id": 20,
        "slug": "thi-cong-noi-that-nha-pho-go-vap.html",
        "title": "Thi Công Nội Thất Nhà Phố Tại Gò Vấp 2023 – Thiết Kế Đột Phá & Thi Công Chuẩn Mực",
        "category": "Dự Án Thực Tế",
        "date": "02/02/2024",
        "iso_date": "2024-02-02",
        "read_time": "8 phút đọc",
        "edition": "Số 20 • Nhà Phố Hiện Đại",
        "meta_desc": "Dự án thi công nội thất nhà phố tại Gò Vấp 2023 bởi Quốc Phan Design: thiết kế tối ưu giếng trời lấy sáng, cầu thang gỗ hiện đại, tủ âm tường tiện nghi.",
        "keywords": "thi công nội thất nhà phố tại gò vấp, nội thất nhà phố gò vấp, thiết kế nhà phố 3 tầng gò vấp, xưởng nội thất quận gò vấp",
        "lead": "Gò Vấp là khu vực tập trung nhiều nhà phố phân lô có chiều dài lớn. Dự án thi công nội thất nhà phố 3 tầng do Quốc Phan thực hiện đã giải quyết hoàn hảo bài toán thông gió và ánh sáng tự nhiên.",
        "toc": [
            ("sec-1", "1. Thiết kế nội thất nhà phố và lên ý tưởng bố trí giếng trời"),
            ("sec-2", "2. Thi công nội thất nhà phố và những lưu ý an toàn kỹ thuật"),
            ("sec-3", "3. Hoàn thiện nội thất gỗ tự nhiên kết hợp gỗ công nghiệp")
        ],
        "content_html": """
            <p>Nhà phố tại Quận Gò Vấp với diện tích sàn 4.5m x 16m gồm 1 trệt 2 lầu được gia chủ giao phó trọn gói cho Quốc Phan Design từ khâu bóc tách hồ sơ thiết kế đến hoàn thiện đồ gỗ tại xưởng.</p>

            <h2 id="sec-1">1. Thiết kế nội thất nhà phố và lên ý tưởng bố trí giếng trời</h2>
            <p>Khoảng giếng trời giữa nhà được tận dụng làm trục đối lưu không khí, kết hợp tiểu cảnh cây xanh và vách gỗ trang trí chạy dài suốt 3 tầng lầu tạo điểm nhấn thị giác vô cùng ấn tượng.</p>

            <!-- <image src="" alt="Phòng khách nhà phố tại Gò Vấp với giếng trời tràn ngập ánh sáng tự nhiên" /> -->

            <h2 id="sec-2">2. Thi công nội thất nhà phố và những lưu ý an toàn kỹ thuật</h2>
            <p>Cầu thang bộ có độ dốc vừa phải, mặt bậc ốp gỗ gõ đỏ tự nhiên chống trơn trượt kết hợp tay vịn gỗ và lan can kính cường lực 10mm thanh thoát, đảm bảo an toàn tuyệt đối cho người già và trẻ nhỏ.</p>

            <!-- <image src="" alt="Hệ tủ bếp gỗ công nghiệp cao cấp thi công tại nhà phố Gò Vấp – Quốc Phan" /> -->
        """
    },
    {
        "id": 21,
        "slug": "tron-goi-noi-that-can-ho-2-phong-ngu-ssr.html",
        "title": "Trọn Gói Nội Thất Căn Hộ 2 Phòng Ngủ SSR (Saigon South Residences) – Đẹp Hiện Đại",
        "category": "Dự Án Thực Tế",
        "date": "05/02/2024",
        "iso_date": "2024-02-05",
        "read_time": "6 phút đọc",
        "edition": "Số 21 • Căn Hộ Phú Mỹ Hưng Nam Sài Gòn",
        "meta_desc": "Gói thi công nội thất căn hộ 2 phòng ngủ Saigon South Residences (SSR) Phú Mỹ Hưng: dự toán trọn gói, thời gian hoàn thiện 12 ngày, bảo hành kết cấu 5 năm.",
        "keywords": "trọn gói nội thất căn hộ 2 phòng ngủ ssr, nội thất saigon south residences, thi công căn hộ ssr, nội thất chung cư ssr quận 7",
        "lead": "Dự án Saigon South Residences (SSR) của chủ đầu tư Phú Mỹ Hưng là cộng đồng dân cư văn minh. Gói thi công nội thất 2PN trọn gói tại đây mang lại sự hài lòng tuyệt đối cho gia chủ.",
        "toc": [
            ("sec-1", "1. Đặc điểm mặt bằng căn hộ 2 phòng ngủ Saigon South Residences"),
            ("sec-2", "2. Bố trí nội thất phòng khách, bếp và 2 phòng ngủ"),
            ("sec-3", "3. Bảng giá trọn gói và tiến độ bàn giao chìa khóa")
        ],
        "content_html": """
            <p>Căn hộ 71m² tại dự án Saigon South Residences (SSR) sở hữu ban công view hồ bơi xanh mát. Gia chủ yêu cầu một gói thi công hoàn thiện trọn gói với chi phí tối ưu nhưng độ bền vật tư phải vượt trội.</p>

            <!-- <image src="" alt="Không gian phòng khách hoàn thiện trọn gói căn hộ 2 phòng ngủ SSR – Quốc Phan Design" /> -->

            <h2 id="sec-1">1. Đặc điểm mặt bằng căn hộ 2 phòng ngủ Saigon South Residences</h2>
            <p>Không gian được thiết kế liên thông giữa bếp chữ L và phòng khách. Hệ tủ giầy kịch trần kết hợp ghế ngồi xỏ giày tiện dụng ngay lối vào giúp giải quyết triệt để sự lộn xộn của mũ bảo hiểm và giày dép.</p>

            <!-- <image src="" alt="Phòng ngủ master ấm cúng với tủ áo cánh lùa tiết kiệm diện tích tại căn hộ SSR" /> -->
        """
    },
    {
        "id": 22,
        "slug": "noi-that-chung-cu-kieu-nhat-japandi.html",
        "title": "Nội Thất Chung Cư Kiểu Nhật 2024 – Phong Cách Japandi Tinh Tế & An Nhiên",
        "category": "Phong Cách Sống",
        "date": "10/02/2024",
        "iso_date": "2024-02-10",
        "read_time": "6 phút đọc",
        "edition": "Số 22 • Phong Cách Japandi",
        "meta_desc": "Thiết kế nội thất chung cư kiểu Nhật phong cách Japandi 2024: sự kết hợp hoàn mỹ giữa mộc mạc Wabi Sabi Nhật Bản và tiện nghi Scandinavian Bắc Âu.",
        "keywords": "nội thất chung cư kiểu nhật 2024, phong cách japandi, thiết kế nội thất wabi sabi, căn hộ phong cách nhật bản",
        "lead": "Japandi là sự giao thoa kỳ diệu giữa văn hóa Wabi Sabi mộc mạc của Nhật Bản và lối sống Hygge ấm cúng Bắc Âu. Một không gian sống đưa tâm hồn bạn về với sự an yên, tĩnh tại.",
        "toc": [
            ("sec-1", "1. Tinh thần cốt lõi của phong cách nội thất Japandi"),
            ("sec-2", "2. Vật liệu tự nhiên: Gỗ sáng màu, mây tre đan và vải lanh linen"),
            ("sec-3", "3. Bố trí chiếu Tatami và bàn trà bệt thư giãn"),
            ("sec-4", "4. Giảm thiểu đồ đạc hướng tới cuộc sống tối giản hạnh phúc")
        ],
        "content_html": """
            <p>Trong nhịp sống đô thị tấp nập, ngày càng nhiều gia đình tìm về với <strong>phong cách nội thất kiểu Nhật (Japandi)</strong>. Không gian được gạn lọc tối đa những chi tiết rườm rà, nhường chỗ cho sự mộc mạc của gỗ sáng màu, ánh sáng tự nhiên và khoảng thở thảnh thơi.</p>

            <h2 id="sec-1">1. Tinh thần cốt lõi của phong cách nội thất Japandi</h2>
            <p>Japandi không chạy theo những gì quá hoàn hảo bóng bẩy. Nó trân trọng vẻ đẹp nguyên bản của vân gỗ tự nhiên, những đường nét vuông vức giản dị nhưng ẩn chứa công năng lưu trữ vô cùng thông minh.</p>

            <!-- <image src="" alt="Phòng khách phong cách Japandi kiểu Nhật với bàn trà bệt và ghế bọc vải thô mộc" /> -->

            <h2 id="sec-2">2. Vật liệu tự nhiên: Gỗ sáng màu, mây tre đan và vải lanh linen</h2>
            <p>Quốc Phan sử dụng gỗ sồi tự nhiên màu sáng (Light Oak) kết hợp các tấm ốp nan gỗ thưa và chi tiết mây mắt cáo đan thủ công trên cánh tủ, tạo nên cảm giác gần gũi, mát mẻ trong khí hậu nhiệt đới Sài Gòn.</p>

            <!-- <image src="" alt="Góc thưởng trà kiểu Nhật với chiếu tatami và vách ngăn shoji truyền thống" /> -->
        """
    },
    {
        "id": 23,
        "slug": "thiet-ke-chung-cu-toi-gian-kieu-nhat.html",
        "title": "Thiết Kế Chung Cư Tối Giản Kiểu Nhật 2024 – Less Is More, Sống Thanh Thản",
        "category": "Phong Cách Sống",
        "date": "14/02/2024",
        "iso_date": "2024-02-14",
        "read_time": "5 phút đọc",
        "edition": "Số 23 • Lối Sống Tối Giản",
        "meta_desc": "Thiết kế chung cư tối giản kiểu Nhật (Minimalism). Nguyên tắc Less is more, đồ nội thất thông minh đa năng, giải phóng không gian sống và nuôi dưỡng bình yên.",
        "keywords": "thiết kế chung cư tối giản kiểu nhật, nội thất tối giản phong cách nhật, căn hộ minimalism, thiết kế nội thất phong cách nhật 2024",
        "lead": "'Less is more - Ít hơn là nhiều hơn'. Khi bạn dọn bớt những đồ đạc thừa thãi khỏi tầm mắt, tâm trí bạn sẽ được giải phóng khỏi những bộn bề lo toan của cuộc sống hiện đại.",
        "toc": [
            ("sec-1", "1. Nguyên tắc 'Ít nhưng chất' trong căn hộ tối giản kiểu Nhật"),
            ("sec-2", "2. Hệ tủ giấu kín cánh phẳng không tay nắm"),
            ("sec-3", "3. Nghệ thuật sử dụng ánh sáng và bóng đổ thiền định")
        ],
        "content_html": """
            <p>Thiết kế nội thất tối giản kiểu Nhật (Minimalism) không có nghĩa là để căn nhà trống rỗng nghèo nàn, mà là sự tính toán tinh vi để mọi đồ đạc sinh hoạt đều được cất giấu khéo léo sau những hệ cánh tủ phẳng liền tường.</p>

            <!-- <image src="" alt="Không gian phòng khách tối giản kiểu Nhật thanh tịnh với tone màu be sáng" /> -->

            <h2 id="sec-1">1. Nguyên tắc 'Ít nhưng chất' trong căn hộ tối giản kiểu Nhật</h2>
            <p>Mỗi món đồ hiện diện trong ngôi nhà đều phải có mục đích rõ ràng và mang lại niềm vui cho gia chủ. Một chiếc sofa bệt êm ái, một chiếc bàn trà thấp bằng gỗ nguyên khối và một bức tranh thủy mặc thiền định là đủ để tạo nên linh hồn cho phòng khách.</p>

            <!-- <image src="" alt="Hệ tủ quần áo kịch trần giấu kín cánh phẳng sơn mờ đồng màu tường phòng ngủ" /> -->
        """
    },
    {
        "id": 24,
        "slug": "thiet-ke-noi-that-chung-cu-90m2-quan-2.html",
        "title": "Thiết Kế Nội Thất Chung Cư 90m2 Tại Quận 2 – 3 Phòng Ngủ Hiện Đại & Đẳng Cấp",
        "category": "Dự Án Thực Tế",
        "date": "18/02/2024",
        "iso_date": "2024-02-18",
        "read_time": "7 phút đọc",
        "edition": "Số 24 • Căn Hộ Cao Cấp TP Thủ Đức",
        "meta_desc": "Dự án thiết kế thi công nội thất căn hộ chung cư 90m2 với 3 phòng ngủ tại Quận 2 (TP Thủ Đức). Không gian mở, ban công xanh, may đo đồ gỗ An Cường trọn gói.",
        "keywords": "thiết kế nội thất chung cư 90m2 tại quận 2, nội thất chung cư quận 2, căn hộ 90m2 3 phòng ngủ quận 2, thi công nội thất tp thủ đức",
        "lead": "Căn hộ 90m2 tại trung tâm Quận 2 (TP. Thủ Đức) sở hữu không gian khoáng đạt. Cùng khám phá phương án thiết kế 3 phòng ngủ hiện đại do KTS Quốc Phan dày công kiến tạo.",
        "toc": [
            ("sec-1", "1. Thông tin tổng quan: Căn hộ chung cư 90m2 tại Quận 2"),
            ("sec-2", "2. Bố trí không gian sinh hoạt chung kết nối đại ban công"),
            ("sec-3", "3. Ba phòng ngủ với phong cách cá nhân hóa riêng biệt"),
            ("sec-4", "4. Báo giá và tiến độ hoàn thiện thực tế tại công trình")
        ],
        "content_html": """
            <p>Quận 2 (nay thuộc TP. Thủ Đức) là tâm điểm của các dự án căn hộ cao cấp với cộng đồng cư dân quốc tế năng động. Căn hộ 90m² được gia chủ đặt hàng Quốc Phan Design thiết kế theo phong cách hiện đại sang trọng (Modern Luxury), tối đa hóa diện tích đón gió sông Sài Gòn mát lành.</p>

            <h2 id="sec-1">1. Thông tin tổng quan: Căn hộ chung cư 90m2 tại Quận 2</h2>
            <p><strong>Loại hình:</strong> Căn hộ chung cư 3 phòng ngủ, 2WC.<br>
            <strong>Diện tích:</strong> 90m² thông thủy.<br>
            <strong>Phong cách:</strong> Hiện đại sang trọng kết hợp gỗ óc chó và đá Marble.<br>
            <strong>Chất liệu chính:</strong> Gỗ MDF lõi xanh chống ẩm An Cường, phụ kiện Hafele Đức.</p>

            <!-- <image src="" alt="Phòng khách căn hộ chung cư 90m2 Quận 2 rộng mở ra ban công thoáng mát" /> -->

            <h2 id="sec-2">2. Bố trí không gian sinh hoạt chung kết nối đại ban công</h2>
            <p>Bàn ăn mặt đá ceramic 6 ghế bọc da cao cấp được bố trí liền kề đảo bếp tạo thành khu vực phục vụ tiệc trà linh hoạt. Hệ đèn chùm thả trần hiện đại làm bừng sáng gian phòng khách.</p>

            <!-- <image src="" alt="Phòng ngủ master căn hộ 90m2 với tủ áo cánh kính âm tường sang trọng" /> -->
        """
    }
]

def build_article_html(post):
    slug = post["slug"]
    title = post["title"]
    category = post["category"]
    date = post["date"]
    iso_date = post["iso_date"]
    read_time = post["read_time"]
    edition = post["edition"]
    meta_desc = post["meta_desc"]
    keywords = post["keywords"]
    lead = post["lead"]
    toc = post["toc"]
    content = post["content_html"]

    # Table of contents HTML
    toc_items = "".join([f'<li><a href="#{tid}">{tlabel}</a></li>' for tid, tlabel in toc])

    # Related articles
    current_idx = post["id"] - 1
    related_posts = []
    for offset in [1, 2, 3]:
        rel_idx = (current_idx + offset) % len(BLOG_POSTS)
        related_posts.append(BLOG_POSTS[rel_idx])

    related_html = "".join([
        f'''
        <a href="{r['slug']}" class="newsletter-related-card">
            <div>
                <div class="category-tiny">{r['category']}</div>
                <h5>{r['title']}</h5>
            </div>
            <div class="date-tiny"><i class="fa fa-calendar"></i> {r['date']} • {r['read_time']}</div>
        </a>
        ''' for r in related_posts
    ])

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <!-- Basic -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">   
   
    <!-- Mobile Metas -->
    <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
 
    <!-- Site Metas -->
    <title>{title} | Công Ty TNHH Thiết Kế Quốc Phan</title>  
    <meta name="keywords" content="{keywords}">
    <meta name="description" content="{meta_desc}">
    <meta name="author" content="Công Ty TNHH Thiết Kế Quốc Phan">
    <link rel="canonical" href="https://quocphan.vn/blog/{slug}">

    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="article">
    <meta property="og:title" content="{title} | Quốc Phan Design">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://quocphan.vn/blog/{slug}">
    <meta property="og:site_name" content="Công Ty TNHH Thiết Kế Quốc Phan">
    <meta property="article:published_time" content="{iso_date}T08:00:00+07:00">
    <meta property="article:author" content="Phan Tiến Quốc">
    <meta property="article:section" content="{category}">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title} | Quốc Phan Design">
    <meta name="twitter:description" content="{meta_desc}">

    <!-- Site Icons -->
    <link rel="shortcut icon" href="../Logo.png" type="image/x-icon" />
    <link rel="apple-touch-icon" href="../Logo.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="../css/bootstrap.min.css">
    <!-- Site CSS -->
    <link rel="stylesheet" href="../style.css">
    <!-- Responsive CSS -->
    <link rel="stylesheet" href="../css/responsive.css">
    <!-- Custom CSS & Vietnamese Fonts -->
    <link rel="stylesheet" href="../css/custom.css">
    <!-- Newsletter Editorial CSS -->
    <link rel="stylesheet" href="../css/newsletter.css">

    <!-- Structured Data JSON-LD (Schema.org BlogPosting) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BlogPosting",
      "mainEntityOfPage": {{
        "@type": "WebPage",
        "@id": "https://quocphan.vn/blog/{slug}"
      }},
      "headline": "{title}",
      "description": "{meta_desc}",
      "author": {{
        "@type": "Organization",
        "name": "Công Ty TNHH Thiết Kế Quốc Phan",
        "url": "https://quocphan.vn"
      }},
      "publisher": {{
        "@type": "Organization",
        "name": "Công Ty TNHH Thiết Kế Quốc Phan",
        "logo": {{
          "@type": "ImageObject",
          "url": "https://quocphan.vn/images/logos/logo.png"
        }}
      }},
      "datePublished": "{iso_date}T08:00:00+07:00",
      "dateModified": "2026-09-10T16:00:00+07:00"
    }}
    </script>
</head>
<body class="newsletter-page">

    <!-- TOP BAR -->
	<div class="top-bar">
		<div class="container-fluid">
			<div class="row" style="display: flex; align-items: center; flex-wrap: wrap;">
				<div class="col-md-6 col-sm-12">
					<span class="company-title">CÔNG TY TNHH THIẾT KẾ QUỐC PHAN</span>
				</div>
				<div class="col-md-6 col-sm-12">
					<div class="top-right-info">
						<span><i class="fa fa-map-marker"></i> 434/34 Bình Quới, Phường 28, Quận Bình Thạnh</span>
						<span class="divider">|</span>
						<a href="mailto:info@quocphan.vn" title="Gửi Email"><i class="fa fa-envelope-o"></i></a>
						<span class="divider">|</span>
						<span title="Giờ làm việc: 08:00 - 18:00"><i class="fa fa-clock-o"></i></span>
						<span class="divider">|</span>
						<a href="tel:0912400503" title="Gọi hotline 0912-400-503"><i class="fa fa-phone"></i></a>
					</div>
				</div>
			</div>
		</div>
	</div>

    <!-- MAIN HEADER -->
    <header class="header header_style_01">
        <nav class="megamenu navbar navbar-default">
            <div class="container-fluid">
                <div class="navbar-header">
                    <a class="navbar-brand" href="../index.html">
                        <img src="../images/logos/logo.png" alt="Quoc Phan Design" class="img-responsive">
                    </a>
                    <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
                        <span class="sr-only">Toggle navigation</span>
                        <span class="toggle-text">Menu</span>
                        <i class="fa fa-angle-down"></i>
                    </button>
                    <div class="mobile-cta-wrapper">
                        <a href="tel:0912400503" class="btn-hotline-mobile" title="Hotline 0912-400-503">
                            <i class="fa fa-phone"></i> <span>0912.400.503</span>
                        </a>
                    </div>
                </div>
                <div id="navbar" class="navbar-collapse collapse">
                    <div class="nav-centered-wrapper">
                        <ul class="nav navbar-nav">
                            <li><a href="../index.html">Trang Chủ</a></li>
                            <li><a href="../gioi-thieu.html">Giới Thiệu</a></li>
                            <li class="dropdown">
                                <a href="../khach-hang.html" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                    Khách Hàng <i class="fa fa-angle-down" style="font-size: 11px; margin-left: 2px;"></i>
                                </a>
                                <ul class="dropdown-menu">
                                    <li>
                                        <a href="../danh-cho-chu-nha.html">
                                            <i class="fa fa-home"></i> Khách Hàng Cá Nhân
                                            <small>Chủ Nhà / Căn Hộ Dịch Vụ (B2C)</small>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="../danh-cho-nha-dau-tu.html">
                                            <i class="fa fa-line-chart"></i> Khách Hàng Doanh Nghiệp
                                            <small>Chủ Đầu Tư Căn Hộ, Homestay, Shophouse</small>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="../danh-cho-doi-tac.html">
                                            <i class="fa fa-handshake-o"></i> Đối Tác B2B
                                            <small>Nhà Thầu, Thiết Kế & Kiến Trúc Sư</small>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                            <li><a href="../noi-that.html">Nội Thất</a></li>
                            <li><a href="../xuong.html">Xưởng</a></li>
                            <li><a href="../bao-gia.html">Báo Giá</a></li>
                            <li><a class="active" href="../blog.html">Blog</a></li>
                            <li><a href="../lien-he.html">Liên Hệ</a></li>
                        </ul>
                    </div>

                    <div class="header-cta-wrapper">
                        <a href="tel:0912400503" class="btn-hotline-header">
                            <i class="fa fa-phone"></i> GỌI NGAY : 0912.400.503
                        </a>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <!-- BANNER & BREADCRUMB -->
    <div class="newsletter-banner">
        <div class="container">
            <ul class="breadcrumb">
                <li><a href="../index.html"><i class="fa fa-home"></i> Trang Chủ</a></li>
                <li><a href="../blog.html">Blog & Cẩm Nang</a></li>
                <li class="active">{category}</li>
            </ul>
        </div>
    </div>

    <!-- MAIN READING CONTENT (SINGLE COLUMN EDITORIAL LAYOUT) -->
    <main class="container newsletter-single-container">
        <article class="newsletter-article-card">
            
            <!-- HEADER -->
            <header class="newsletter-header">
                <div class="newsletter-meta-top">
                    <span class="newsletter-category-badge"><i class="fa fa-tag"></i> {category}</span>
                    <span class="newsletter-edition-info">{edition}</span>
                </div>
                <h1 class="newsletter-title">{title}</h1>
                <div class="newsletter-byline">
                    <img src="../Logo.png" alt="Quốc Phan Design" class="author-avatar">
                    <div>
                        <span class="author-name">KTS. Phan Tiến Quốc</span> &bull; <span>Ban Biên Tập Quốc Phan</span>
                        <div style="font-size:12px; margin-top:2px;">
                            <span><i class="fa fa-calendar"></i> {date}</span>
                            <span class="separator">|</span>
                            <span><i class="fa fa-clock-o"></i> {read_time}</span>
                            <span class="separator">|</span>
                            <span><i class="fa fa-check-circle" style="color:#c86443;"></i> Nội dung đã kiểm duyệt chuyên môn</span>
                        </div>
                    </div>
                </div>
            </header>

            <!-- LEAD / SUMMARY BOX -->
            <div class="newsletter-lead-box">
                <i class="fa fa-quote-left" style="color:var(--nl-terracotta); margin-right:8px;"></i>
                {lead}
            </div>

            <!-- TABLE OF CONTENTS -->
            <div class="newsletter-toc">
                <div class="newsletter-toc-title">
                    <i class="fa fa-list-ul"></i> Mục Lục Bài Viết
                </div>
                <ul>
                    {toc_items}
                </ul>
            </div>

            <!-- BODY CONTENT WITH INTEGRATED <IMAGE> PLACEHOLDERS -->
            <div class="newsletter-content">
                {content}
            </div>

            <!-- INTERNAL LINKING / SERVICE HUB -->
            <div class="newsletter-hub-links">
                <h4><i class="fa fa-link"></i> Dịch Vụ Liên Quan Tại Xưởng Quốc Phan</h4>
                <ul>
                    <li><a href="../xuong.html"><i class="fa fa-industry" style="color:#8b6f5d;"></i> Tham quan quy mô Xưởng sản xuất đồ gỗ 1000m² tại Bình Thạnh</a></li>
                    <li><a href="../bao-gia.html"><i class="fa fa-calculator" style="color:#8b6f5d;"></i> Xem bảng báo giá thi công nội thất chìa khóa trao tay 2026</a></li>
                    <li><a href="../noi-that.html"><i class="fa fa-cube" style="color:#8b6f5d;"></i> Các bộ sưu tập nội thất căn hộ & tủ bếp may đo mới nhất</a></li>
                    <li><a href="../danh-cho-chu-nha.html"><i class="fa fa-user-circle" style="color:#8b6f5d;"></i> Chính sách hỗ trợ dành riêng cho khách hàng chủ nhà (B2C)</a></li>
                </ul>
            </div>

            <!-- AUTHOR BIO BOX -->
            <div class="newsletter-author-box">
                <img src="../Logo.png" alt="Công Ty TNHH Thiết Kế Quốc Phan">
                <div class="newsletter-author-info">
                    <h4>Công Ty TNHH Thiết Kế Quốc Phan</h4>
                    <p>Thương hiệu chuyên sâu về tư vấn thiết kế kiến trúc và trực tiếp sản xuất nội thất gỗ công nghiệp chuẩn An Cường từ năm 2017. Trụ sở & Xưởng sản xuất tại 434/34 Bình Quới, Phường 28, Quận Bình Thạnh, TP.HCM.</p>
                </div>
            </div>

            <!-- NEWSLETTER SUBSCRIPTION & ZALO CTA BOX -->
            <div class="newsletter-cta-box">
                <h3>Đăng Ký Nhận Cẩm Nang & Tư Vấn Báo Giá Tại Xưởng</h3>
                <p>Nhận ngay bộ cẩm nang kinh nghiệm làm nội thất chống ẩm và bảng dự toán chi tiết từng mét ván gỗ trực tiếp từ Kiến trúc sư trưởng Quốc Phan Design.</p>
                <div class="newsletter-cta-actions">
                    <a href="https://zalo.me/g/anqvwcclatvb9lgtxzcn" target="_blank" rel="noopener noreferrer" class="btn-newsletter-cta">
                        <i class="fa fa-comments"></i> Tham Gia Nhóm Zalo Tư Vấn Miễn Phí
                    </a>
                    <a href="tel:0912400503" class="btn-newsletter-secondary">
                        <i class="fa fa-phone"></i> Hotline: 0912.400.503
                    </a>
                </div>
            </div>

            <!-- RELATED ISSUES FEED -->
            <div class="newsletter-related-wrap">
                <div class="newsletter-related-title">
                    <i class="fa fa-newspaper-o" style="color:var(--nl-terracotta);"></i> Các Số Bản Tin Cùng Chuyên Mục
                </div>
                <div class="newsletter-related-grid">
                    {related_html}
                </div>
            </div>

        </article>
    </main>

    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-5 col-sm-12 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <img src="../images/logos/logo.png" alt="Quoc Phan Design" style="max-height: 48px; margin-bottom: 15px; border-radius: 4px;">
                            <h3>CÔNG TY TNHH THIẾT KẾ QUỐC PHAN</h3>
                        </div>
                        <p>Thương hiệu chuyên sâu về thiết kế kiến trúc, hoàn thiện nội thất và sản xuất đồ gỗ thủ công mỹ nghệ cao cấp. Chúng tôi kiến tạo không gian sống tiện nghi, sang trọng và bền vững theo thời gian.</p>
                        
                        <div class="footer-company-meta">
                            <ul class="footer-links">
                                <li><i class="fa fa-id-card-o"></i> <strong>Mã số thuế:</strong> <span style="color:#f7d59c; font-weight:700;">0314372672</span></li>
                                <li><i class="fa fa-calendar-check-o"></i> <strong>Ngày bắt đầu hoạt động:</strong> 26/04/2017 (2017-04-26)</li>
                                <li><i class="fa fa-map-marker"></i> <strong>Địa chỉ trụ sở:</strong> 434/34 Bình Quới, Phường 28, Quận Bình Thạnh, TP. Hồ Chí Minh</li>
                                <li><i class="fa fa-industry"></i> <strong>Xưởng sản xuất:</strong> Quy mô 1000m² - Máy móc CNC tự động hóa</li>
                                <li><i class="fa fa-phone"></i> <strong>Hotline:</strong> <a href="tel:0912400503" style="color: #f7d59c; font-weight:700;">0912-400-503</a></li>
                                <li><i class="fa fa-comments"></i> <strong>Nhóm Zalo:</strong> <a href="https://zalo.me/g/anqvwcclatvb9lgtxzcn" target="_blank" rel="noopener noreferrer" style="color: #64b5f6; font-weight: 700;">Tham Gia Nhóm Tư Vấn</a></li>
                                <li><i class="fa fa-envelope"></i> <strong>Email:</strong> <a href="mailto:info@quocphan.vn">info@quocphan.vn</a></li>
                                <li><i class="fa fa-globe"></i> <strong>Website:</strong> quocphan.vn</li>
                            </ul>
                        </div>
                    </div>
                </div>

                <div class="col-md-3 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Truyền Thông & Tiện Ích</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="../blog.html"><i class="fa fa-newspaper-o" style="margin-right:6px;"></i> Bản Tin Kiến Trúc & Xưởng</a></li>
                            <li><a href="../sitemap.xml" target="_blank"><i class="fa fa-sitemap" style="margin-right:6px;"></i> Sơ Đồ Web (Sitemap)</a></li>
                            <li><a href="../llms.txt" target="_blank"><i class="fa fa-file-text-o" style="margin-right:6px;"></i> Hồ Sơ AI (llms.txt)</a></li>
                            <li><a href="../gioi-thieu.html"><i class="fa fa-trophy" style="margin-right:6px;"></i> Năng Lực 100% Made in VN</a></li>
                            <li><a href="../bao-gia.html"><i class="fa fa-calculator" style="margin-right:6px;"></i> Dự Toán Báo Giá Online</a></li>
                            <li><a href="../lien-he.html"><i class="fa fa-shield" style="margin-right:6px;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                        </ul>
                    </div>
                </div>

                <div class="col-md-4 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Danh Mục Chuyên Trang</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="../index.html">Trang Chủ <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../gioi-thieu.html">Giới Thiệu <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../khach-hang.html">Khách Hàng <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../noi-that.html">Nội Thất <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../xuong.html">Xưởng Sản Xuất <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../bao-gia.html">Báo Giá Thi Công <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../blog.html">Blog & Cẩm Nang <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="../lien-he.html">Liên Hệ Trực Tiếp <span class="icon icon-arrow-right2"></span></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </footer>

    <div class="copyrights">
        <div class="container">
            <div class="footer-distributed">
                <div class="footer-left">                   
                    <p class="footer-company-name">Bản quyền &copy; 2026 <a href="../index.html">Công Ty TNHH Thiết Kế Quốc Phan</a> (quocphan.vn). Tất cả các quyền được bảo lưu.</p>
                </div>
            </div>
        </div>
    </div>

    <a href="#" id="scroll-to-top" class="dmtop global-radius"><i class="fa fa-angle-up"></i></a>

    <!-- FLOATING ZALO WIDGET -->
    <div class="qp-floating-zalo" id="qpZaloFloat">
        <a href="https://zalo.me/g/anqvwcclatvb9lgtxzcn" target="_blank" rel="noopener noreferrer" class="qp-zalo-link" title="Tham gia nhóm Zalo tư vấn Quoc Phan Design">
            <span class="qp-zalo-pulse"></span>
            <span class="qp-zalo-pulse-2"></span>
            <div class="qp-zalo-icon-box">
                <img src="../zalo.png" alt="Zalo Quoc Phan Design" class="qp-zalo-img">
            </div>
            <div class="qp-zalo-text-badge">
                <span class="qp-zalo-title">Nhóm Zalo</span>
                <span class="qp-zalo-subtitle">Tư vấn báo giá</span>
            </div>
        </a>
    </div>

    <!-- ALL JS FILES -->
    <script src="../js/all.js"></script>
    <script src="../js/custom.js"></script>
</body>
</html>
"""
    return html

def main():
    os.makedirs("blog", exist_ok=True)
    generated_count = 0
    for post in BLOG_POSTS:
        filepath = os.path.join("blog", post["slug"])
        html_content = build_article_html(post)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
        generated_count += 1
        print(f"[{generated_count}/24] Created {filepath}")
    print(f"Successfully generated all {generated_count} newsletter blog posts in blog/")

if __name__ == "__main__":
    main()
