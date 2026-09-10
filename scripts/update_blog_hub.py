"""
Script to generate the updated, Newsletter-styled blog.html hub page
containing all 24 articles with interactive search and category filtering.
"""

from generate_all_blogs import BLOG_POSTS

def generate_blog_hub():
    category_groups = {
        "all": "Tất Cả (24)",
        "xuong-bep": "Xưởng & Tủ Bếp",
        "can-ho": "Căn Hộ Chung Cư",
        "du-an": "Dự Án Thực Tế",
        "cam-nang": "Xu Hướng & Báo Giá"
    }

    def get_group(cat):
        if cat in ["Xưởng Sản Xuất", "Tủ Bếp"]:
            return "xuong-bep"
        elif cat in ["Căn Hộ Chung Cư", "Phòng Ngủ"]:
            return "can-ho"
        elif cat in ["Dự Án Thực Tế"]:
            return "du-an"
        else:
            return "cam-nang"

    cards_html = []
    for post in BLOG_POSTS:
        group = get_group(post["category"])
        card = f"""
        <article class="newsletter-feed-item" data-category="{group}" data-title="{post['title'].lower()}" data-desc="{post['meta_desc'].lower()}">
            <div class="feed-item-top">
                <div class="feed-item-meta">
                    <span class="feed-item-category"><i class="fa fa-tag"></i> {post['category']}</span>
                    <span><i class="fa fa-calendar"></i> {post['date']}</span>
                </div>
                <h3 class="feed-item-title">
                    <a href="blog/{post['slug']}">{post['title']}</a>
                </h3>
                <p class="feed-item-excerpt">{post['lead']}</p>
            </div>
            <div class="feed-item-footer">
                <span class="feed-read-time"><i class="fa fa-clock-o"></i> {post['read_time']}</span>
                <a href="blog/{post['slug']}" class="feed-read-more">Đọc bản tin &rarr;</a>
            </div>
        </article>
        """
        cards_html.append(card)

    cards_joined = "".join(cards_html)

    # JSON-LD ItemList
    item_list_elements = []
    for idx, p in enumerate(BLOG_POSTS):
        item_list_elements.append(f"""
        {{{{
          "@type": "ListItem",
          "position": {idx + 1},
          "url": "https://quocphan.vn/blog/{p['slug']}",
          "name": "{p['title']}"
        }}}}""")
    json_ld_items = ",".join(item_list_elements)

    html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
    <!-- Basic -->
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">   
   
    <!-- Mobile Metas -->
    <meta name="viewport" content="width=device-width, minimum-scale=1.0, maximum-scale=1.0, user-scalable=no">
 
    <!-- Site Metas -->
    <title>Bản Tin & Cẩm Nang Nội Thất | Công Ty TNHH Thiết Kế Quốc Phan</title>  
    <meta name="keywords" content="Blog Quoc Phan Design, cẩm nang nội thất, kinh nghiệm làm nội thất bình thạnh, tủ bếp an cường, thi công căn hộ chung cư, báo giá làm nội thất">
    <meta name="description" content="Chuyên mục Bản Tin & Cẩm Nang Nội Thất Quốc Phan Design - Nơi chia sẻ 24 số cẩm nang chuyên sâu về xưởng sản xuất đồ gỗ, thi công tủ bếp, căn hộ và kinh nghiệm hoàn thiện nhà phố.">
    <meta name="author" content="Công Ty TNHH Thiết Kế Quốc Phan">
    <link rel="canonical" href="https://quocphan.vn/blog.html">

    <!-- Open Graph -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="Bản Tin & Cẩm Nang Nội Thất | Quốc Phan Design">
    <meta property="og:description" content="Tổng hợp 24 số bản tin kinh nghiệm thi công nội thất, thiết kế tủ bếp, căn hộ chung cư trực tiếp từ xưởng sản xuất Quốc Phan Bình Thạnh.">
    <meta property="og:url" content="https://quocphan.vn/blog.html">
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
    <!-- Newsletter Editorial CSS -->
    <link rel="stylesheet" href="css/newsletter.css">

    <!-- Modernizer for Portfolio -->
    <script src="js/modernizer.js"></script>

    <!-- Structured Data JSON-LD (Schema.org CollectionPage) -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "CollectionPage",
      "name": "Bản Tin & Cẩm Nang Nội Thất Quốc Phan Design",
      "description": "Trung tâm lưu trữ các bài viết chuyên đề cẩm nang thiết kế và thi công đồ gỗ nội thất.",
      "url": "https://quocphan.vn/blog.html",
      "mainEntity": {{
        "@type": "ItemList",
        "itemListElement": [{json_ld_items}
        ]
      }}
    }}
    </script>
</head>
<body class="newsletter-page">

    <!-- PRELOADER (BREATHING LOGO) -->
    <div id="preloader">
        <div class="preloader-content">
            <img src="images/logos/logo.png" alt="Công Ty TNHH Thiết Kế Quốc Phan" class="preloader-logo">
            <div class="preloader-line"></div>
        </div>
    </div><!-- end preloader -->
    
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
                            <li><a class="active" href="blog.html">Blog</a></li>
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

    <!-- NEWSLETTER HERO HEADER -->
    <div class="newsletter-hub-hero">
        <div class="container">
            <span class="hub-badge"><i class="fa fa-newspaper-o"></i> Editorial & Knowledge Hub</span>
            <h1>Bản Tin & Cẩm Nang Nội Thất</h1>
            <p>Tuyển tập 24 số cẩm nang chuyên sâu về xưởng sản xuất đồ gỗ, kinh nghiệm hoàn thiện căn hộ, thi công tủ bếp và báo giá trực tiếp từ Kiến trúc sư Quốc Phan Design.</p>
        </div>
    </div>

    <!-- MAIN CONTENT AREA -->
    <div class="container">
        
        <!-- SEARCH & CATEGORY FILTER BAR -->
        <div class="newsletter-filter-bar">
            <div class="newsletter-filter-pills" id="categoryFilterPills">
                <button class="filter-pill active" data-filter="all">Tất Cả (24)</button>
                <button class="filter-pill" data-filter="xuong-bep"><i class="fa fa-industry"></i> Xưởng & Tủ Bếp</button>
                <button class="filter-pill" data-filter="can-ho"><i class="fa fa-building-o"></i> Căn Hộ Chung Cư</button>
                <button class="filter-pill" data-filter="du-an"><i class="fa fa-check-square-o"></i> Dự Án Thực Tế</button>
                <button class="filter-pill" data-filter="cam-nang"><i class="fa fa-lightbulb-o"></i> Xu Hướng & Báo Giá</button>
            </div>
            <div class="newsletter-search-box">
                <input type="text" id="blogSearchInput" placeholder="Tìm kiếm bài viết, từ khóa...">
                <i class="fa fa-search"></i>
            </div>
        </div>

        <!-- NO RESULTS MESSAGE (HIDDEN BY DEFAULT) -->
        <div id="noResultsMsg" style="display:none; text-align:center; padding:50px 20px; background:#fff; border:1px dashed #ded5cb; border-radius:10px; margin-bottom:40px;">
            <i class="fa fa-search" style="font-size:36px; color:#a98d79; margin-bottom:12px;"></i>
            <h4 style="font-weight:700; color:#3d2616;">Không tìm thấy bài viết phù hợp</h4>
            <p style="color:#666;">Vui lòng thử lại với từ khóa khác như: tủ bếp, căn hộ, báo giá, bình thạnh...</p>
        </div>

        <!-- FEED GRID: 24 NEWSLETTER CARDS -->
        <div class="newsletter-feed-grid" id="newsletterFeedGrid">
            {cards_joined}
        </div>

        <!-- NEWSLETTER SIGNUP BOX -->
        <div class="newsletter-cta-box" style="margin-bottom:60px;">
            <h3>Bạn Cần Tư Vấn Thiết Kế Hoặc Đóng Đồ Gỗ Trực Tiếp Tại Xưởng?</h3>
            <p>Kiến trúc sư Quốc Phan Design sẵn sàng hỗ trợ khảo sát hiện trạng tận nơi và lên phương án dự toán tối ưu ngân sách hoàn toàn miễn phí.</p>
            <div class="newsletter-cta-actions">
                <a href="https://zalo.me/g/anqvwcclatvb9lgtxzcn" target="_blank" rel="noopener noreferrer" class="btn-newsletter-cta">
                    <i class="fa fa-comments"></i> Tham Gia Nhóm Zalo Tư Vấn Miễn Phí
                </a>
                <a href="tel:0912400503" class="btn-newsletter-secondary">
                    <i class="fa fa-phone"></i> Gọi Hotline: 0912.400.503
                </a>
            </div>
        </div>

    </div>

    <!-- FOOTER -->
    <footer class="footer">
        <div class="container">
            <div class="row">
                <div class="col-md-5 col-sm-12 col-xs-12">
                    <div class="widget clearfix">
                        <div class="widget-title">
                            <img src="images/logos/logo.png" alt="Quoc Phan Design" style="max-height: 48px; margin-bottom: 15px; border-radius: 4px;">
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
                            <li><a href="blog.html"><i class="fa fa-newspaper-o" style="margin-right:6px;"></i> Bản Tin Kiến Trúc & Xưởng</a></li>
                            <li><a href="sitemap.xml" target="_blank"><i class="fa fa-sitemap" style="margin-right:6px;"></i> Sơ Đồ Web (Sitemap)</a></li>
                            <li><a href="llms.txt" target="_blank"><i class="fa fa-file-text-o" style="margin-right:6px;"></i> Hồ Sơ AI (llms.txt)</a></li>
                            <li><a href="gioi-thieu.html"><i class="fa fa-trophy" style="margin-right:6px;"></i> Năng Lực 100% Made in VN</a></li>
                            <li><a href="bao-gia.html"><i class="fa fa-calculator" style="margin-right:6px;"></i> Dự Toán Báo Giá Online</a></li>
                            <li><a href="lien-he.html"><i class="fa fa-shield" style="margin-right:6px;"></i> Chính Sách Bảo Hành 5 Năm</a></li>
                        </ul>
                    </div>
                </div>

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

    <!-- ALL JS FILES -->
    <script src="js/all.js"></script>
    <script src="js/custom.js"></script>

    <!-- CLIENT-SIDE FILTER & LIVE SEARCH SCRIPT -->
    <script>
    document.addEventListener("DOMContentLoaded", function() {{
        var searchInput = document.getElementById("blogSearchInput");
        var filterPills = document.querySelectorAll("#categoryFilterPills .filter-pill");
        var feedItems = document.querySelectorAll(".newsletter-feed-item");
        var noResults = document.getElementById("noResultsMsg");

        var activeCategory = "all";
        var searchTerm = "";

        function filterBlogs() {{
            var visibleCount = 0;
            feedItems.forEach(function(item) {{
                var itemCat = item.getAttribute("data-category");
                var itemTitle = item.getAttribute("data-title") || "";
                var itemDesc = item.getAttribute("data-desc") || "";

                var matchesCat = (activeCategory === "all" || itemCat === activeCategory);
                var matchesSearch = (!searchTerm || itemTitle.indexOf(searchTerm) !== -1 || itemDesc.indexOf(searchTerm) !== -1);

                if (matchesCat && matchesSearch) {{
                    item.style.display = "flex";
                    visibleCount++;
                }} else {{
                    item.style.display = "none";
                }}
            }});

            if (visibleCount === 0) {{
                noResults.style.display = "block";
            }} else {{
                noResults.style.display = "none";
            }}
        }}

        filterPills.forEach(function(pill) {{
            pill.addEventListener("click", function() {{
                filterPills.forEach(function(p) {{ p.classList.remove("active"); }});
                this.classList.add("active");
                activeCategory = this.getAttribute("data-filter");
                filterBlogs();
            }});
        }});

        if (searchInput) {{
            searchInput.addEventListener("input", function() {{
                searchTerm = this.value.trim().toLowerCase();
                filterBlogs();
            }});
        }}
    }});
    </script>
</body>
</html>
"""
    with open("blog.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("Successfully updated blog.html with Newsletter Archive layout!")

if __name__ == "__main__":
    generate_blog_hub()
