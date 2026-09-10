"""
Script to create the 6 mandatory compliance & press pages for Quoc Phan Design (quocphan.vn)
conforming to the Ministry of Industry and Trade (Bo Cong Thuong) website notification guidelines.
"""

import os

FOOTER_HTML = """
    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <div class="row">
                <!-- CỘT 1: GIỚI THIỆU & THÔNG TIN PHÁP LÝ DOANH NGHIỆP -->
                <div class="col-md-5 col-sm-12 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <img src="images/logos/logo.png" alt="Quoc Phan Design" style="max-height: 48px; margin-bottom: 15px; border-radius: 4px;">
                            <h3>CÔNG TY TNHH THIẾT KẾ QUỐC PHAN</h3>
                        </div>
                        <p>Thương hiệu chuyên sâu về thiết kế kiến trúc, hoàn thiện nội thất và sản xuất đồ gỗ thủ công mỹ nghệ cao cấp. Chúng tôi kiến tạo không gian sống tiện nghi, sang trọng và bền vững theo thời gian.</p>
                        
                        <div class="footer-company-meta">
                            <ul class="footer-links">
                                <li><i class="fa fa-id-card-o"></i> <strong>Mã số thuế:</strong> <span style="color:#f7d59c; font-weight:700;">0314372672</span> (Do Sở KH&ĐT TP.HCM cấp ngày 26/04/2017)</li>
                                <li><i class="fa fa-user"></i> <strong>Người đại diện pháp luật:</strong> <span style="color:#f7d59c; font-weight:700;">Ông Phan Tiến Quốc</span></li>
                                <li><i class="fa fa-map-marker"></i> <strong>Địa chỉ trụ sở:</strong> 434/34 Bình Quới, Phường 28, Quận Bình Thạnh, TP. Hồ Chí Minh</li>
                                <li><i class="fa fa-industry"></i> <strong>Xưởng sản xuất:</strong> Quy mô 1000m² - Máy móc CNC tự động hóa</li>
                                <li><i class="fa fa-phone"></i> <strong>Hotline:</strong> <a href="tel:0912400503" style="color: #f7d59c; font-weight:700;">0912-400-503</a></li>
                                <li><i class="fa fa-comments"></i> <strong>Nhóm Zalo:</strong> <a href="https://zalo.me/g/anqvwcclatvb9lgtxzcn" target="_blank" rel="noopener noreferrer" style="color: #64b5f6; font-weight: 700;">Tham Gia Nhóm Tư Vấn</a></li>
                                <li><i class="fa fa-envelope"></i> <strong>Email:</strong> <a href="mailto:info@quocphan.vn">info@quocphan.vn</a></li>
                                <li><i class="fa fa-globe"></i> <strong>Website:</strong> quocphan.vn</li>
                            </ul>
                        </div>

                        <!-- HUY HIỆU BỘ CÔNG THƯƠNG (THỦ TỤC THÔNG BÁO) -->
                        <div style="margin-top: 20px;">
                            <a href="http://online.gov.vn" target="_blank" rel="noopener noreferrer" style="display:inline-flex; align-items:center; gap:10px; background:rgba(255,255,255,0.06); padding:8px 15px; border-radius:6px; border:1px solid rgba(255,255,255,0.18); text-decoration:none;" title="Website đang tiến hành thủ tục thông báo với Bộ Công Thương theo quy định TMĐT">
                                <i class="fa fa-shield" style="color:#64b5f6; font-size:22px;"></i>
                                <div style="text-align:left; line-height:1.25;">
                                    <span style="display:block; font-size:10px; color:#e0d7cf; text-transform:uppercase; letter-spacing:0.5px;">Thủ tục thông báo TMĐT</span>
                                    <span style="font-size:12.5px; color:#f7d59c; font-weight:700;">BỘ CÔNG THƯƠNG</span>
                                </div>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- CỘT 2: TRUYỀN THÔNG & TIỆN ÍCH (CHỨA ĐẦY ĐỦ CÁC TRANG CHÍNH SÁCH BỘ CÔNG THƯƠNG & QUAN HỆ BÁO CHÍ) -->
                <div class="col-md-3 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Truyền Thông & Tiện Ích</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="quan-he-bao-chi.html"><i class="fa fa-bullhorn" style="margin-right:6px;"></i> Quan Hệ Báo Chí</a></li>
                            <li><a href="chinh-sach-bao-mat.html"><i class="fa fa-lock" style="margin-right:6px;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html"><i class="fa fa-credit-card" style="margin-right:6px;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html"><i class="fa fa-wrench" style="margin-right:6px;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html"><i class="fa fa-truck" style="margin-right:6px;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html"><i class="fa fa-file-text-o" style="margin-right:6px;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                            <li><a href="blog.html"><i class="fa fa-newspaper-o" style="margin-right:6px;"></i> Bản Tin Kiến Trúc & Xưởng</a></li>
                            <li><a href="sitemap.xml" target="_blank"><i class="fa fa-sitemap" style="margin-right:6px;"></i> Sơ Đồ Web (Sitemap)</a></li>
                            <li><a href="llms.txt" target="_blank"><i class="fa fa-file-code-o" style="margin-right:6px;"></i> Hồ Sơ AI (llms.txt)</a></li>
                        </ul>
                    </div>
                </div>

                <!-- CỘT 3: DANH MỤC CHUYÊN TRANG -->
                <div class="col-md-4 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Danh Mục Chuyên Trang</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="index.html">Trang Chủ <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="gioi-thieu.html">Giới Thiệu <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="khach-hang.html">Khách Hàng <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="noi-that.html">Nội Thất <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="xuong.html">Xưởng Sản Xuất <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="bao-gia.html">Báo Giá Thi Công <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="blog.html">Blog & Cẩm Nang <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="lien-he.html">Liên Hệ Trực Tiếp <span class="icon icon-arrow-right2"></span></a></li>
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
                    <p class="footer-company-name">Bản quyền &copy; 2026 <a href="index.html">Công Ty TNHH Thiết Kế Quốc Phan</a> (quocphan.vn). Tất cả các quyền được bảo lưu.</p>
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
                <img src="zalo.png" alt="Zalo Quoc Phan Design" class="qp-zalo-img">
            </div>
            <div class="qp-zalo-text-badge">
                <span class="qp-zalo-title">Nhóm Zalo</span>
                <span class="qp-zalo-subtitle">Tư vấn báo giá</span>
            </div>
        </a>
    </div>
"""

HEADER_HTML = """
    <!-- PRELOADER (BREATHING LOGO) -->
    <div id="preloader">
        <div class="preloader-content">
            <img src="images/logos/logo.png" alt="Công Ty TNHH Thiết Kế Quốc Phan" class="preloader-logo">
            <div class="preloader-line"></div>
        </div>
    </div>
    
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
                    <a class="navbar-brand" href="index.html">
                        <img src="images/logos/logo.png" alt="Quoc Phan Design" class="img-responsive">
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
                            <li><a href="index.html">Trang Chủ</a></li>
                            <li><a href="gioi-thieu.html">Giới Thiệu</a></li>
                            <li class="dropdown">
                                <a href="khach-hang.html" class="dropdown-toggle" data-toggle="dropdown" role="button" aria-haspopup="true" aria-expanded="false">
                                    Khách Hàng <i class="fa fa-angle-down" style="font-size: 11px; margin-left: 2px;"></i>
                                </a>
                                <ul class="dropdown-menu">
                                    <li>
                                        <a href="danh-cho-chu-nha.html">
                                            <i class="fa fa-home"></i> Khách Hàng Cá Nhân
                                            <small>Chủ Nhà / Căn Hộ Dịch Vụ (B2C)</small>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="danh-cho-nha-dau-tu.html">
                                            <i class="fa fa-line-chart"></i> Khách Hàng Doanh Nghiệp
                                            <small>Chủ Đầu Tư Căn Hộ, Homestay, Shophouse</small>
                                        </a>
                                    </li>
                                    <li>
                                        <a href="danh-cho-doi-tac.html">
                                            <i class="fa fa-handshake-o"></i> Đối Tác B2B
                                            <small>Nhà Thầu, Thiết Kế & Kiến Trúc Sư</small>
                                        </a>
                                    </li>
                                </ul>
                            </li>
                            <li><a href="noi-that.html">Nội Thất</a></li>
                            <li><a href="xuong.html">Xưởng</a></li>
                            <li><a href="bao-gia.html">Báo Giá</a></li>
                            <li><a href="blog.html">Blog</a></li>
                            <li><a href="lien-he.html">Liên Hệ</a></li>
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
"""

PAGES_CONFIG = [
    {
        "filename": "quan-he-bao-chi.html",
        "title": "Quan Hệ Báo Chí & Truyền Thông (Press & Media)",
        "meta_desc": "Chuyên mục Quan Hệ Báo Chí Công Ty TNHH Thiết Kế Quốc Phan: thông cáo báo chí, tư liệu truyền thông, bộ nhận diện thương hiệu và thông tin người phát ngôn chính thức.",
        "breadcrumb": "Quan Hệ Báo Chí",
        "h1": "Quan Hệ Báo Chí & Truyền Thông",
        "content": """
            <div class="row">
                <div class="col-md-8 col-sm-12">
                    <div class="policy-content" style="background:#fff; padding:35px 40px; border:1px solid #ebe5df; border-radius:10px; margin-bottom:30px;">
                        <h2 style="color:#3d2616; font-size:24px; font-weight:800; margin-bottom:20px; border-bottom:2px solid #8b6f5d; padding-bottom:10px;">
                            <i class="fa fa-bullhorn" style="color:#c86443;"></i> Thông Tin Báo Chí & Giới Truyền Thông
                        </h2>
                        <p class="lead" style="font-size:16px; color:#55483f; line-height:1.8;">
                            Chào mừng quý nhà báo, phóng viên và các đối tác truyền thông đến với Cổng thông tin <strong>Quan Hệ Báo Chí</strong> của <strong>Công Ty TNHH Thiết Kế Quốc Phan (Quoc Phan Design)</strong>. Tại đây, chúng tôi cung cấp các tư liệu xác thực về quá trình hình thành, năng lực xưởng mộc 1000m² tại Bình Thạnh và các nhận định chuyên môn từ Kiến trúc sư trưởng.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">1. Hồ Sơ Báo Chí Tóm Tắt (Fast Facts)</h3>
                        <ul style="line-height:2; font-size:15px; color:#444;">
                            <li><strong>Tên đầy đủ:</strong> CÔNG TY TNHH THIẾT KẾ QUỐC PHAN</li>
                            <li><strong>Thương hiệu thương mại:</strong> Quốc Phan Design (quocphan.vn)</li>
                            <li><strong>Mã số doanh nghiệp:</strong> 0314372672 (Cấp ngày 26/04/2017 bởi Sở KH&ĐT TP.HCM)</li>
                            <li><strong>Người đại diện pháp luật kiêm người phát ngôn:</strong> Ông Phan Tiến Quốc</li>
                            <li><strong>Trụ sở & Xưởng sản xuất:</strong> 434/34 Bình Quới, Phường 28, Quận Bình Thạnh, TP.HCM</li>
                            <li><strong>Lĩnh vực hoạt động:</strong> Thiết kế kiến trúc, sản xuất gia công đồ gỗ nội thất công nghiệp chuẩn An Cường và thi công hoàn thiện căn hộ, nhà phố, biệt thự chìa khóa trao tay.</li>
                        </ul>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">2. Định Vị Thương Hiệu: 100% Tự Chủ Xưởng Sản Xuất</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Khác biệt với các công ty thiết kế thương mại đóng vai trò trung gian môi giới, Quốc Phan kiên định mô hình <strong>100% Made in Vietnam</strong> với xưởng sản xuất trực tiếp khép kín. Việc làm chủ hệ thống máy cắt CNC tự động hóa, buồng phun sơn cách bụi và dây chuyền dán cạnh nẹp nhiệt giúp doanh nghiệp cung cấp giải pháp đồ gỗ may đo đạt chuẩn kỹ thuật cao với giá thành cạnh tranh từ 20% - 30% so với showroom thị trường.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">3. Tư Liệu Truyền Thông & Media Kit</h3>
                        <div style="background:#fcfaf7; border:1px solid #e5dfd7; border-radius:8px; padding:20px; margin:20px 0;">
                            <h4 style="font-weight:700; color:#3d2616; margin-bottom:10px;"><i class="fa fa-download" style="color:#8b6f5d;"></i> Tải Tư Liệu Báo Chí Chính Thức:</h4>
                            <ul style="list-style:none; padding:0; margin:0; line-height:2.2;">
                                <li><i class="fa fa-file-image-o" style="color:#c86443;"></i> <strong>Logo chuẩn Vector & PNG:</strong> Bản sắc nhận diện thương hiệu Quốc Phan Design (<a href="Logo.png" target="_blank" style="color:#8b6f5d; font-weight:600;">Xem Logo</a>)</li>
                                <li><i class="fa fa-file-pdf-o" style="color:#c86443;"></i> <strong>Hồ sơ năng lực công ty (Company Profile):</strong> Quy mô xưởng máy, các công trình tiêu biểu từ 2017 đến nay.</li>
                                <li><i class="fa fa-file-text-o" style="color:#c86443;"></i> <strong>Hồ sơ dữ liệu số (AI & Semantic Profile):</strong> Định dạng dữ liệu mở theo chuẩn llmstxt.org (<a href="llms.txt" target="_blank" style="color:#8b6f5d; font-weight:600;">Xem llms.txt</a>)</li>
                            </ul>
                        </div>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">4. Đầu Mối Liên Hệ Dành Riêng Cho Báo Chí</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Đối với các yêu cầu phỏng vấn chuyên gia, cung cấp hình ảnh công trình thực tế độ phân giải cao hoặc khảo sát thị trường ngành nội thất gỗ, xin vui lòng liên hệ trực tiếp:
                        </p>
                        <div style="background:#3d2616; color:#ffffff; padding:20px 25px; border-radius:8px; margin-top:15px;">
                            <p style="margin:0 0 8px 0; color:#f7d59c; font-weight:700; font-size:16px;">BAN TRUYỀN THÔNG & QUAN HỆ BÁO CHÍ - QUOC PHAN DESIGN</p>
                            <p style="margin:0 0 5px 0; font-size:14px; color:#e0d7cf;"><i class="fa fa-user"></i> Người phụ trách: Ban Biên Tập & KTS. Phan Tiến Quốc</p>
                            <p style="margin:0 0 5px 0; font-size:14px; color:#e0d7cf;"><i class="fa fa-envelope-o"></i> Email tiếp nhận: <a href="mailto:info@quocphan.vn" style="color:#ffffff; text-decoration:underline;">info@quocphan.vn</a> (Tiêu đề: [Báo Chí] - Tên cơ quan báo chí)</p>
                            <p style="margin:0; font-size:14px; color:#e0d7cf;"><i class="fa fa-phone"></i> Hotline trực tiếp: <a href="tel:0912400503" style="color:#f7d59c; font-weight:700;">0912-400-503</a> (08:00 - 18:00 các ngày làm việc)</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 col-sm-12">
                    <div style="background:#fff; border:1px solid #ebe5df; border-radius:10px; padding:25px; margin-bottom:25px;">
                        <h4 style="font-weight:700; color:#3d2616; border-bottom:2px solid #8b6f5d; padding-bottom:8px;">Chuyên Mục Pháp Lý</h4>
                        <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
                            <li><a href="chinh-sach-bao-mat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                        </ul>
                    </div>

                    <div style="background:#fdfbf8; border:1px dashed #8b6f5d; border-radius:10px; padding:25px; text-align:center;">
                        <h4 style="font-weight:700; color:#3d2616;">Bạn Cần Tư Vấn Thiết Kế?</h4>
                        <p style="font-size:13.5px; color:#666;">Kiến trúc sư Quốc Phan Design hỗ trợ khảo sát tận nơi và dự toán miễn phí.</p>
                        <a href="tel:0912400503" class="btn btn-primary-qp" style="background:#c86443; border-color:#c86443; color:#fff; font-size:13px; font-weight:700;">
                            <i class="fa fa-phone"></i> Gọi 0912.400.503
                        </a>
                    </div>
                </div>
            </div>
        """
    },
    {
        "filename": "chinh-sach-bao-mat.html",
        "title": "Chính Sách Bảo Mật Thông Tin Khách Hàng",
        "meta_desc": "Chính sách bảo mật thông tin khách hàng Công Ty TNHH Thiết Kế Quốc Phan. Tuân thủ nghiêm ngặt Nghị định 52/2013/NĐ-CP và Nghị định 13/2023/NĐ-CP về bảo vệ dữ liệu cá nhân.",
        "breadcrumb": "Chính Sách Bảo Mật",
        "h1": "Chính Sách Bảo Mật Thông Tin",
        "content": """
            <div class="row">
                <div class="col-md-8 col-sm-12">
                    <div class="policy-content" style="background:#fff; padding:35px 40px; border:1px solid #ebe5df; border-radius:10px; margin-bottom:30px;">
                        <h2 style="color:#3d2616; font-size:24px; font-weight:800; margin-bottom:20px; border-bottom:2px solid #8b6f5d; padding-bottom:10px;">
                            <i class="fa fa-lock" style="color:#c86443;"></i> Chính Sách Bảo Mật Thông Tin Khách Hàng
                        </h2>
                        <p style="font-size:15px; color:#555; line-height:1.8;">
                            Căn cứ theo <strong>Nghị định số 52/2013/NĐ-CP</strong> và <strong>Nghị định số 85/2021/NĐ-CP</strong> của Chính phủ về Thương mại điện tử, cùng <strong>Nghị định số 13/2023/NĐ-CP</strong> về bảo vệ dữ liệu cá nhân, <strong>Công Ty TNHH Thiết Kế Quốc Phan</strong> cam kết bảo mật tuyệt đối mọi dữ liệu cá nhân mà khách hàng cung cấp.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">1. Mục Đích & Phạm Vi Thu Thập Thông Tin</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Các thông tin thu thập qua website quocphan.vn bao gồm: Họ tên khách hàng, số điện thoại liên lạc, địa chỉ email, địa chỉ công trình cần khảo sát thi công nội thất. Việc thu thập này chỉ nhằm phục vụ:
                        </p>
                        <ul style="line-height:2; font-size:15px; color:#444;">
                            <li>Liên hệ tư vấn giải pháp thiết kế kiến trúc và dự toán báo giá may đo nội thất.</li>
                            <li>Cử kiến trúc sư và kỹ sư xuống hiện trạng công trình khảo sát đo đạc thực tế.</li>
                            <li>Gửi hợp đồng thi công, hồ sơ bản vẽ 3D và tiến độ sản xuất tại xưởng.</li>
                            <li>Thực hiện nghĩa vụ bảo hành 5 năm và bảo trì kỹ thuật định kỳ.</li>
                        </ul>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">2. Phạm Vi Sử Dụng & Thời Gian Lưu Trữ Thông Tin</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Thông tin cá nhân của khách hàng chỉ được sử dụng nội bộ trong phạm vi các phòng ban phụ trách (Thiết kế, Kế toán, Xưởng sản xuất, Đội ngũ kỹ thuật bảo hành). Dữ liệu sẽ được lưu trữ an toàn trong hệ thống dữ liệu doanh nghiệp trong suốt thời gian khách hàng sử dụng dịch vụ và trong suốt thời hạn bảo hành 5 năm của công trình.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">3. Cam Kết Tuyệt Đối Không Tiết Lộ Cho Bên Thứ Ba</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Công Ty TNHH Thiết Kế Quốc Phan cam kết không bán, chia sẻ hoặc trao đổi thông tin cá nhân của khách hàng cho bất kỳ bên thứ ba nào vì mục đích thương mại. Thông tin chỉ được cung cấp khi có yêu cầu bằng văn bản từ cơ quan tư pháp hoặc cơ quan quản lý nhà nước có thẩm quyền theo quy định của pháp luật Việt Nam.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">4. Đơn Vị Thu Thập & Quản Lý Dữ Liệu Cá Nhân</h3>
                        <div style="background:#fcfaf7; border:1px solid #e5dfd7; border-radius:8px; padding:20px; line-height:1.9; font-size:14.5px; color:#444;">
                            <p style="margin:0;"><strong>CÔNG TY TNHH THIẾT KẾ QUỐC PHAN</strong></p>
                            <p style="margin:0;">Mã số thuế: 0314372672</p>
                            <p style="margin:0;">Địa chỉ: 434/34 Bình Quới, Phường 28, Quận Bình Thạnh, TP. Hồ Chí Minh</p>
                            <p style="margin:0;">Email: info@quocphan.vn | Hotline: 0912-400-503</p>
                        </div>
                    </div>
                </div>

                <div class="col-md-4 col-sm-12">
                    <div style="background:#fff; border:1px solid #ebe5df; border-radius:10px; padding:25px; margin-bottom:25px;">
                        <h4 style="font-weight:700; color:#3d2616; border-bottom:2px solid #8b6f5d; padding-bottom:8px;">Chuyên Mục Pháp Lý</h4>
                        <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
                            <li><a href="quan-he-bao-chi.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quan Hệ Báo Chí</a></li>
                            <li><a href="chinh-sach-bao-mat.html" style="color:#c86443; font-weight:700;"><i class="fa fa-angle-right" style="color:#c86443;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        """
    },
    {
        "filename": "chinh-sach-thanh-toan.html",
        "title": "Chính Sách & Quy Định Thanh Toán",
        "meta_desc": "Chính sách và quy định thanh toán tại Công Ty TNHH Thiết Kế Quốc Phan. Phương thức thanh toán linh hoạt qua tiền mặt hoặc chuyển khoản công ty theo từng giai đoạn nghiệm thu.",
        "breadcrumb": "Chính Sách Thanh Toán",
        "h1": "Chính Sách & Quy Định Thanh Toán",
        "content": """
            <div class="row">
                <div class="col-md-8 col-sm-12">
                    <div class="policy-content" style="background:#fff; padding:35px 40px; border:1px solid #ebe5df; border-radius:10px; margin-bottom:30px;">
                        <h2 style="color:#3d2616; font-size:24px; font-weight:800; margin-bottom:20px; border-bottom:2px solid #8b6f5d; padding-bottom:10px;">
                            <i class="fa fa-credit-card" style="color:#c86443;"></i> Quy Định & Phương Thức Thanh Toán
                        </h2>
                        <p style="font-size:15px; color:#555; line-height:1.8;">
                            Để tạo sự thuận tiện và minh bạch tài chính tối đa cho khách hàng khi thực hiện hợp đồng thiết kế và thi công sản xuất nội thất, <strong>Công Ty TNHH Thiết Kế Quốc Phan</strong> áp dụng các phương thức và tiến độ thanh toán chuẩn mực dưới đây:
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">1. Các Phương Thức Thanh Toán Được Chấp Nhận</h3>
                        <div style="background:#fcfaf7; border:1px solid #e5dfd7; border-radius:8px; padding:20px; margin-bottom:20px;">
                            <p style="font-size:15px; line-height:1.8; color:#444;"><strong>A. Thanh toán bằng tiền mặt:</strong> Khách hàng có thể thanh toán trực tiếp tại Trụ sở/Văn phòng công ty (434/34 Bình Quới, P.28, Q.Bình Thạnh) hoặc thanh toán cho nhân viên thu ngân có giấy giới thiệu và phiếu thu đóng dấu mộc công ty.</p>
                            <p style="font-size:15px; line-height:1.8; color:#444; margin-top:12px;"><strong>B. Thanh toán qua Chuyển Khoản Ngân Hàng (Khuyến khích):</strong> Quý khách chuyển khoản vào tài khoản ngân hàng chính thức của Công ty hoặc người đại diện pháp luật theo đúng cú pháp hợp đồng.</p>
                        </div>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">2. Tiến Độ Thanh Toán Theo Hợp Đồng Thi Công Sản Xuất</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Để giảm thiểu rủi ro cho gia chủ, chi phí thi công may đo đồ gỗ nội thất được chia thành 3 đợt tương ứng với từng mốc nghiệm thu thực tế:
                        </p>
                        <ul style="line-height:2; font-size:15px; color:#444;">
                            <li><strong>Đợt 1 (Tạm ứng ký hợp đồng - 40% giá trị hợp đồng):</strong> Thực hiện sau khi hai bên ký kết hợp đồng thi công và chốt bản vẽ sản xuất 2D/3D chi tiết để xưởng nhập phôi gỗ An Cường và tiến hành gia công CNC.</li>
                            <li><strong>Đợt 2 (Giao hàng đến công trình - 40% giá trị hợp đồng):</strong> Thực hiện khi toàn bộ kiện hàng đồ gỗ được vận chuyển đến hiện trạng công trình của khách hàng và được hai bên kiểm đếm đầy đủ trước khi lắp ráp.</li>
                            <li><strong>Đợt 3 (Nghiệm thu bàn giao - 20% còn lại):</strong> Thực hiện sau khi đội ngũ thợ mộc hoàn tất lắp ráp, dọn dẹp vệ sinh công nghiệp và hai bên ký biên bản nghiệm thu bàn giao chìa khóa trao tay.</li>
                        </ul>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">3. Xuất Hóa Đơn Giá Trị Gia Tăng (VAT)</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Đối với khách hàng doanh nghiệp, công ty cổ phần hoặc chủ đầu tư cần xuất hóa đơn tài chính, Quốc Phan Design xuất hóa đơn điện tử hợp pháp theo đúng quy định của Tổng cục Thuế trong vòng 03 ngày làm việc kể từ ngày nghiệm thu bàn giao.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-12">
                    <div style="background:#fff; border:1px solid #ebe5df; border-radius:10px; padding:25px; margin-bottom:25px;">
                        <h4 style="font-weight:700; color:#3d2616; border-bottom:2px solid #8b6f5d; padding-bottom:8px;">Chuyên Mục Pháp Lý</h4>
                        <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
                            <li><a href="quan-he-bao-chi.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quan Hệ Báo Chí</a></li>
                            <li><a href="chinh-sach-bao-mat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html" style="color:#c86443; font-weight:700;"><i class="fa fa-angle-right" style="color:#c86443;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        """
    },
    {
        "filename": "chinh-sach-bao-hanh-bao-tri.html",
        "title": "Chính Sách Bảo Hành 5 Năm & Bảo Trì Đồ Gỗ",
        "meta_desc": "Chính sách bảo hành 5 năm kết cấu đồ gỗ nội thất và bảo trì trọn đời tại Quốc Phan Design. Cam kết có mặt xử lý sự cố trong 24 giờ tại TP. Hồ Chí Minh.",
        "breadcrumb": "Chính Sách Bảo Hành",
        "h1": "Chính Sách Bảo Hành & Bảo Trì 5 Năm",
        "content": """
            <div class="row">
                <div class="col-md-8 col-sm-12">
                    <div class="policy-content" style="background:#fff; padding:35px 40px; border:1px solid #ebe5df; border-radius:10px; margin-bottom:30px;">
                        <h2 style="color:#3d2616; font-size:24px; font-weight:800; margin-bottom:20px; border-bottom:2px solid #8b6f5d; padding-bottom:10px;">
                            <i class="fa fa-wrench" style="color:#c86443;"></i> Chính Sách Bảo Hành 5 Năm & Bảo Trì Dài Hạn
                        </h2>
                        <p style="font-size:15px; color:#555; line-height:1.8;">
                            Với phương châm <em>"Chất lượng tạo dựng niềm tin"</em>, <strong>Công Ty TNHH Thiết Kế Quốc Phan</strong> tự tin áp dụng chế độ bảo hành dài hạn lên đến <strong>05 năm</strong> cho toàn bộ kết cấu đồ gỗ do chính xưởng mộc Quốc Phan trực tiếp sản xuất.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">1. Thời Hạn & Phạm Vi Bảo Hành</h3>
                        <ul style="line-height:2; font-size:15px; color:#444;">
                            <li><strong>Bảo hành 05 năm đối với kết cấu gỗ:</strong> Áp dụng cho các lỗi kỹ thuật do sản xuất như co ngót, nứt nẻ, bong tróc nẹp chỉ dán cạnh, cong vênh bản lề trong điều kiện sử dụng bình thường.</li>
                            <li><strong>Bảo hành theo hãng đối với phụ kiện kim khí:</strong> Các phụ kiện ray trượt giảm chấn, bản lề, tay nâng tủ bếp chính hãng Hafele, Blum, Eurogold được bảo hành từ 02 đến 05 năm theo quy định của nhà phân phối.</li>
                            <li><strong>Bảo trì trọn đời sản phẩm:</strong> Sau thời hạn bảo hành 5 năm, Quốc Phan tiếp tục hỗ trợ sửa chữa, cân chỉnh cánh tủ hoặc thay mới linh kiện với mức giá gốc ưu đãi.</li>
                        </ul>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">2. Các Trường Hợp Không Thuộc Diện Bảo Hành Miễn Phí</h3>
                        <ul style="line-height:2; font-size:15px; color:#444;">
                            <li>Hư hỏng do tác động ngoại lực bất thường (va đập mạnh, rơi vỡ, vật nhọn làm xước bề mặt).</li>
                            <li>Sản phẩm bị ngâm nước do sự cố rò rỉ đường ống nước của tòa nhà hoặc thiên tai ngập lụt.</li>
                            <li>Khách hàng tự ý tháo dỡ, sửa chữa hoặc di dời đồ gỗ mà không thông báo cho kỹ thuật viên Quốc Phan.</li>
                        </ul>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">3. Quy Trình & Thời Gian Xử Lý Sự Cố Trong 24 Giờ</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Khi phát hiện sự cố cần khắc phục, khách hàng chỉ cần gọi điện trực tiếp đến Hotline <strong>0912-400-503</strong> hoặc nhắn tin vào nhóm Zalo tư vấn kèm hình ảnh/video. Đội ngũ kỹ thuật viên của xưởng Quốc Phan cam kết có mặt tại công trình trong vòng <strong>24 giờ làm việc</strong> để kiểm tra và xử lý triệt để.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-12">
                    <div style="background:#fff; border:1px solid #ebe5df; border-radius:10px; padding:25px; margin-bottom:25px;">
                        <h4 style="font-weight:700; color:#3d2616; border-bottom:2px solid #8b6f5d; padding-bottom:8px;">Chuyên Mục Pháp Lý</h4>
                        <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
                            <li><a href="quan-he-bao-chi.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quan Hệ Báo Chí</a></li>
                            <li><a href="chinh-sach-bao-mat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html" style="color:#c86443; font-weight:700;"><i class="fa fa-angle-right" style="color:#c86443;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        """
    },
    {
        "filename": "chinh-sach-giao-hang-lap-dat.html",
        "title": "Chính Sách Vận Chuyển & Giao Nhận Lắp Đặt",
        "meta_desc": "Chính sách vận chuyển và giao nhận lắp đặt đồ gỗ nội thất tại Quốc Phan Design: quy chuẩn đóng gói bọc màng PE chống trầy, giao hàng an toàn toàn khu vực TP.HCM.",
        "breadcrumb": "Chính Sách Giao Nhận",
        "h1": "Chính Sách Vận Chuyển & Giao Nhận Lắp Đặt",
        "content": """
            <div class="row">
                <div class="col-md-8 col-sm-12">
                    <div class="policy-content" style="background:#fff; padding:35px 40px; border:1px solid #ebe5df; border-radius:10px; margin-bottom:30px;">
                        <h2 style="color:#3d2616; font-size:24px; font-weight:800; margin-bottom:20px; border-bottom:2px solid #8b6f5d; padding-bottom:10px;">
                            <i class="fa fa-truck" style="color:#c86443;"></i> Quy Trình Vận Chuyển & Lắp Đặt Tại Công Trình
                        </h2>
                        <p style="font-size:15px; color:#555; line-height:1.8;">
                            Để đảm bảo từng khối tủ áo, tủ bếp và vách ốp trang trí đến tay khách hàng luôn trong tình trạng hoàn hảo nguyên vẹn, <strong>Công Ty TNHH Thiết Kế Quốc Phan</strong> thực hiện quy trình giao nhận và lắp đặt nghiêm ngặt theo các tiêu chuẩn:
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">1. Quy Chuẩn Đóng Gói Bảo Vệ Sản Phẩm Xuất Xưởng</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Mỗi sản phẩm đồ gỗ trước khi rời xưởng mộc Bình Thạnh đều được quấn màng co PE bảo vệ chống ẩm, bọc xốp bóng khí (bubble wrap) và nẹp góc bìa carton cứng cáp ở các vị trí dễ va quẹt.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">2. Phạm Vi Giao Hàng & Chi Phí Vận Chuyển</h3>
                        <ul style="line-height:2; font-size:15px; color:#444;">
                            <li><strong>Khu vực TP. Hồ Chí Minh:</strong> Miễn phí 100% chi phí vận chuyển cho các đơn hàng thi công nội thất căn hộ và nhà phố trọn gói.</li>
                            <li><strong>Các tỉnh thành lân cận (Bình Dương, Đồng Nai, Long An, Bà Rịa - Vũng Tàu):</strong> Hỗ trợ chi phí vận chuyển theo biểu phí xe tải thực tế với mức giá tối ưu nhất.</li>
                        </ul>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">3. Quy Trình Lắp Ráp & Vệ Sinh Bàn Giao</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Đội ngũ thợ mộc của Quốc Phan tuân thủ quy định đăng ký thi công của Ban quản lý tòa nhà, bọc lót sàn gỗ hiện hữu, giảm thiểu tiếng ồn và dọn dẹp vệ sinh sạch sẽ mặt bằng trước khi bàn giao cho gia chủ.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-12">
                    <div style="background:#fff; border:1px solid #ebe5df; border-radius:10px; padding:25px; margin-bottom:25px;">
                        <h4 style="font-weight:700; color:#3d2616; border-bottom:2px solid #8b6f5d; padding-bottom:8px;">Chuyên Mục Pháp Lý</h4>
                        <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
                            <li><a href="quan-he-bao-chi.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quan Hệ Báo Chí</a></li>
                            <li><a href="chinh-sach-bao-mat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html" style="color:#c86443; font-weight:700;"><i class="fa fa-angle-right" style="color:#c86443;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        """
    },
    {
        "filename": "dieu-khoan-dich-vu.html",
        "title": "Quy Định Sử Dụng Dịch Vụ & Điều Khoản Giao Dịch Chung",
        "meta_desc": "Điều khoản dịch vụ và quy định giao dịch chung tại Công Ty TNHH Thiết Kế Quốc Phan. Quy định trách nhiệm các bên, quy trình đặt hàng và nghiệm thu hoàn thiện nội thất.",
        "breadcrumb": "Điều Khoản Dịch Vụ",
        "h1": "Quy Định & Điều Khoản Dịch Vụ",
        "content": """
            <div class="row">
                <div class="col-md-8 col-sm-12">
                    <div class="policy-content" style="background:#fff; padding:35px 40px; border:1px solid #ebe5df; border-radius:10px; margin-bottom:30px;">
                        <h2 style="color:#3d2616; font-size:24px; font-weight:800; margin-bottom:20px; border-bottom:2px solid #8b6f5d; padding-bottom:10px;">
                            <i class="fa fa-file-text-o" style="color:#c86443;"></i> Điều Khoản Dịch Vụ & Quy Trình Giao Dịch Chung
                        </h2>
                        <p style="font-size:15px; color:#555; line-height:1.8;">
                            Khi truy cập website quocphan.vn hoặc ký kết hợp đồng dịch vụ thiết kế thi công nội thất với <strong>Công Ty TNHH Thiết Kế Quốc Phan</strong>, khách hàng được bảo đảm quyền lợi tối đa và đồng thuận tuân thủ các quy định giao dịch chung dưới đây:
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">1. Quy Trình 5 Bước Thực Hiện Dịch Vụ Khép Kín</h3>
                        <ol style="line-height:2.2; font-size:15px; color:#444; padding-left:20px;">
                            <li><strong>Bước 1 - Tiếp nhận & Tư vấn sơ bộ:</strong> Lắng nghe nhu cầu, sở thích và định hướng ngân sách của khách hàng qua Hotline, Zalo hoặc trực tiếp tại văn phòng.</li>
                            <li><strong>Bước 2 - Khảo sát hiện trạng thực tế:</strong> Kiến trúc sư xuống công trình đo đạc diện tích, kiểm tra hệ thống điện nước, độ ẩm tường và góc vuông hiện trạng.</li>
                            <li><strong>Bước 3 - Lên phối cảnh 3D & Bóc tách dự toán:</strong> Dựng bản vẽ mô phỏng 3D chi tiết và lập bảng báo giá bóc tách khối lượng minh bạch theo từng mét vuông / mét dài.</li>
                            <li><strong>Bước 4 - Sản xuất tại xưởng Quốc Phan:</strong> Gia công đồ gỗ trực tiếp bằng máy CNC tự động hóa, kiểm định chất lượng phôi gỗ trước khi xuất xưởng.</li>
                            <li><strong>Bước 5 - Lắp đặt & Nghiệm thu bàn giao:</strong> Thi công hoàn thiện tại công trình, bàn giao phiếu bảo hành 5 năm và hướng dẫn sử dụng đồ gỗ.</li>
                        </ol>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">2. Quyền & Nghĩa Vụ Của Đôi Bên</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            <strong>Quốc Phan Design:</strong> Cam kết sử dụng đúng chủng loại vật liệu (gỗ MDF lõi xanh An Cường chính hãng, phụ kiện Hafele/Blum), thi công đúng tiến độ thỏa thuận và bảo hành theo đúng hợp đồng.<br>
                            <strong>Khách hàng:</strong> Cung cấp thông tin hiện trạng chính xác, tạo điều kiện thuận lợi cho đội ngũ kỹ thuật ra vào công trình và thực hiện thanh toán theo đúng tiến độ các đợt thỏa thuận.
                        </p>

                        <h3 style="color:#3d2616; font-weight:700; margin-top:30px; font-size:19px;">3. Cơ Chế Tiếp Nhận & Giải Quyết Khiếu Nại</h3>
                        <p style="font-size:15px; line-height:1.8; color:#555;">
                            Mọi thắc mắc, phản ánh hoặc khiếu nại về thái độ phục vụ hay chất lượng sản phẩm đều được Ban Giám Đốc tiếp nhận trực tiếp qua Hotline <strong>0912-400-503</strong> hoặc Email: <strong>info@quocphan.vn</strong> và giải quyết dứt điểm trong vòng 24 - 48 giờ làm việc.
                        </p>
                    </div>
                </div>

                <div class="col-md-4 col-sm-12">
                    <div style="background:#fff; border:1px solid #ebe5df; border-radius:10px; padding:25px; margin-bottom:25px;">
                        <h4 style="font-weight:700; color:#3d2616; border-bottom:2px solid #8b6f5d; padding-bottom:8px;">Chuyên Mục Pháp Lý</h4>
                        <ul style="list-style:none; padding:0; margin:0; line-height:2.2; font-size:14px;">
                            <li><a href="quan-he-bao-chi.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Quan Hệ Báo Chí</a></li>
                            <li><a href="chinh-sach-bao-mat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="chinh-sach-thanh-toan.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Thanh Toán</a></li>
                            <li><a href="chinh-sach-bao-hanh-bao-tri.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                            <li><a href="chinh-sach-giao-hang-lap-dat.html" style="color:#555;"><i class="fa fa-angle-right" style="color:#8b6f5d;"></i> Chính Sách Giao Nhận Lắp Đặt</a></li>
                            <li><a href="dieu-khoan-dich-vu.html" style="color:#c86443; font-weight:700;"><i class="fa fa-angle-right" style="color:#c86443;"></i> Quy Định & Điều Khoản Dịch Vụ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
        """
    }
]

def build_page_html(cfg):
    filename = cfg["filename"]
    title = cfg["title"]
    meta_desc = cfg["meta_desc"]
    breadcrumb = cfg["breadcrumb"]
    h1 = cfg["h1"]
    content = cfg["content"]

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
    <meta name="keywords" content="{title}, Công Ty TNHH Thiết Kế Quốc Phan, quy định bộ công thương, pháp lý quoc phan design">
    <meta name="description" content="{meta_desc}">
    <meta name="author" content="Công Ty TNHH Thiết Kế Quốc Phan">
    <link rel="canonical" href="https://quocphan.vn/{filename}">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title} | Quốc Phan Design">
    <meta property="og:description" content="{meta_desc}">
    <meta property="og:url" content="https://quocphan.vn/{filename}">
    <meta property="og:site_name" content="Công Ty TNHH Thiết Kế Quốc Phan">

    <!-- Site Icons -->
    <link rel="shortcut icon" href="Logo.png" type="image/x-icon" />
    <link rel="apple-touch-icon" href="Logo.png">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="css/bootstrap.min.css">
    <!-- Site CSS -->
    <link rel="stylesheet" href="style.css">
    <!-- Responsive CSS -->
    <link rel="stylesheet" href="css/responsive.css">
    <!-- Custom CSS & Vietnamese Fonts -->
    <link rel="stylesheet" href="css/custom.css">

    <!-- Modernizer for Portfolio -->
    <script src="js/modernizer.js"></script>

    <!-- Structured Data JSON-LD -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{title}",
      "description": "{meta_desc}",
      "url": "https://quocphan.vn/{filename}",
      "publisher": {{
        "@type": "Organization",
        "name": "Công Ty TNHH Thiết Kế Quốc Phan",
        "url": "https://quocphan.vn",
        "logo": "https://quocphan.vn/images/logos/logo.png"
      }}
    }}
    </script>
</head>
<body>

{HEADER_HTML}

   	<div class="banner-area banner-bg-1">
		<div class="container">
			<div class="row">
				<div class="col-md-12">
					<div class="banner">
						<h2>{h1}</h2>
						<ul class="page-title-link">
							<li><a href="index.html">Trang Chủ</a></li>
							<li><a href="{filename}">{breadcrumb}</a></li>
						</ul>
					</div>
				</div>
			</div>
		</div>
	</div>

    <div class="section wb">
        <div class="container">
            {content}
        </div>
    </div>

{FOOTER_HTML}

    <!-- ALL JS FILES -->
    <script src="js/all.js"></script>
    <script src="js/custom.js"></script>

</body>
</html>
"""
    return html

def main():
    for cfg in PAGES_CONFIG:
        filepath = cfg["filename"]
        html = build_page_html(cfg)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html)
        print(f"Created compliance page: {filepath}")

if __name__ == "__main__":
    main()
