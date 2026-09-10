import os
import re
import glob

def get_footer_html(prefix=""):
    return f'''    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <div class="row">
                <!-- CỘT 1: THÔNG TIN DOANH NGHIỆP & PHÁP LÝ (BỘ CÔNG THƯƠNG COMPLIANT) -->
                <div class="col-md-4 col-sm-12 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <img src="{prefix}images/logos/logo.png" alt="Quoc Phan Design" style="max-height: 48px; margin-bottom: 15px; border-radius: 8px;">
                            <h3 style="font-size: 16px; line-height: 22px;">CÔNG TY TNHH THIẾT KẾ QUỐC PHAN</h3>
                        </div>
                        <p style="font-size: 13px; line-height: 20px; margin-bottom: 12px;">Đơn vị tổng thầu chuyên sâu về thiết kế kiến trúc, sản xuất nội thất và thi công hoàn thiện trọn gói với xưởng gỗ trực tiếp 1000m² tại TP.HCM.</p>
                        
                        <div class="footer-company-meta">
                            <ul class="footer-links" style="font-size: 12.5px; line-height: 22px;">
                                <li><i class="fa fa-id-card-o"></i> <strong>MST:</strong> <span style="color:#f7d59c; font-weight:700;">0314372672</span> (Sở KH&ĐT TP.HCM cấp 26/04/2017)</li>
                                <li><i class="fa fa-user"></i> <strong>Đại diện pháp luật:</strong> Ông Phan Tiến Quốc</li>
                                <li><i class="fa fa-map-marker"></i> <strong>Trụ sở chính:</strong> 434/34 Bình Quới, Phường 28, Q. Bình Thạnh, TP.HCM</li>
                                <li><i class="fa fa-industry"></i> <strong>Xưởng sản xuất:</strong> 52 Đường 27, P. Linh Đông, TP. Thủ Đức, TP.HCM</li>
                                <li><i class="fa fa-phone"></i> <strong>Hotline:</strong> <a href="tel:0912400503" style="color: #f7d59c; font-weight:700;">0912-400-503</a></li>
                                <li><i class="fa fa-envelope"></i> <strong>Email:</strong> <a href="mailto:info@quocphan.vn">info@quocphan.vn</a></li>
                            </ul>
                        </div>
                        
                        <!-- DẤU ĐĂNG KÝ BỘ CÔNG THƯƠNG PLACEHOLDER -->
                        <div style="margin-top: 15px;">
                            <a href="http://online.gov.vn" target="_blank" rel="noopener noreferrer" style="display: inline-block; border: 1px solid rgba(247, 213, 156, 0.35); padding: 8px 12px; border-radius: 6px; background: rgba(0,0,0,0.25); color: #fff; text-decoration: none; font-size: 12px; transition: all 0.3s ease;">
                                <i class="fa fa-shield" style="color: #4caf50; font-size: 15px; margin-right: 6px; vertical-align: middle;"></i>
                                <span style="vertical-align: middle; color: #f7d59c; font-weight: 600;">ĐÃ THÔNG BÁO BỘ CÔNG THƯƠNG</span>
                            </a>
                        </div>
                    </div>
                </div>

                <!-- CỘT 2: TRUYỀN THÔNG & TIỆN ÍCH -->
                <div class="col-md-3 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Truyền Thông & Tiện Ích</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="{prefix}quan-he-bao-chi.html"><i class="fa fa-bullhorn" style="margin-right:6px; color:#f7d59c;"></i> Quan Hệ Báo Chí & Media Kit</a></li>
                            <li><a href="{prefix}blog.html"><i class="fa fa-newspaper-o" style="margin-right:6px;"></i> Bản Tin Kiến Trúc & Xưởng</a></li>
                            <li><a href="{prefix}bao-gia.html"><i class="fa fa-calculator" style="margin-right:6px;"></i> Dự Toán Báo Giá Online</a></li>
                            <li><a href="{prefix}xuong.html"><i class="fa fa-industry" style="margin-right:6px;"></i> Năng Lực Xưởng Gỗ 1000m²</a></li>
                            <li><a href="{prefix}sitemap.xml" target="_blank"><i class="fa fa-sitemap" style="margin-right:6px;"></i> Sơ Đồ Website (Sitemap)</a></li>
                            <li><a href="{prefix}llms.txt" target="_blank"><i class="fa fa-file-text-o" style="margin-right:6px;"></i> Hồ Sơ AI Knowledge (llms.txt)</a></li>
                        </ul>
                    </div>
                </div>

                <!-- CỘT 3: CHÍNH SÁCH & QUY ĐỊNH (CHUẨN BỘ CÔNG THƯƠNG) -->
                <div class="col-md-3 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Chính Sách & Quy Định</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="{prefix}chinh-sach-bao-mat.html"><i class="fa fa-lock" style="margin-right:6px; color:#f7d59c;"></i> Chính Sách Bảo Mật</a></li>
                            <li><a href="{prefix}chinh-sach-thanh-toan.html"><i class="fa fa-credit-card" style="margin-right:6px; color:#f7d59c;"></i> Quy Định Thanh Toán</a></li>
                            <li><a href="{prefix}chinh-sach-bao-hanh-bao-tri.html"><i class="fa fa-shield" style="margin-right:6px; color:#f7d59c;"></i> Bảo Hành 5 Năm & Đổi Trả</a></li>
                            <li><a href="{prefix}chinh-sach-giao-hang-lap-dat.html"><i class="fa fa-truck" style="margin-right:6px; color:#f7d59c;"></i> Vận Chuyển & Lắp Đặt</a></li>
                            <li><a href="{prefix}dieu-khoan-dich-vu.html"><i class="fa fa-file-text-o" style="margin-right:6px; color:#f7d59c;"></i> Điều Khoản Dịch Vụ Mua Bán</a></li>
                        </ul>
                    </div>
                </div>

                <!-- CỘT 4: DANH MỤC CHUYÊN TRANG -->
                <div class="col-md-2 col-sm-6 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <h3>Chuyên Trang</h3>
                        </div>
                        <ul class="footer-links hov">
                            <li><a href="{prefix}index.html">Trang Chủ <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="{prefix}gioi-thieu.html">Giới Thiệu <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="{prefix}noi-that.html">Nội Thất <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="{prefix}xuong.html">Xưởng Gỗ <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="{prefix}bao-gia.html">Báo Giá <span class="icon icon-arrow-right2"></span></a></li>
                            <li><a href="{prefix}lien-he.html">Liên Hệ <span class="icon icon-arrow-right2"></span></a></li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </footer>'''

def update_file(file_path, prefix=""):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_footer = get_footer_html(prefix)
    
    # Replace existing footer block: <!-- FOOTER --> ... </footer> or <footer class="footer">...</footer>
    pattern = r'(<!-- FOOTER -->\s*)?<footer class=["\']footer["\']>.*?</footer>'
    if re.search(pattern, content, re.DOTALL):
        updated_content = re.sub(pattern, new_footer.strip(), content, flags=re.DOTALL)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Updated footer in: {file_path}")
    else:
        print(f"WARNING: Footer not matched in: {file_path}")

def main():
    root_files = glob.glob("*.html")
    for f in root_files:
        update_file(f, prefix="")

    blog_files = glob.glob("blog/*.html")
    for f in blog_files:
        update_file(f, prefix="../")

if __name__ == "__main__":
    main()
