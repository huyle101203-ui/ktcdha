# KTCĐHA – Thư viện Kỹ thuật Chẩn đoán Hình ảnh

Website độc lập xây dựng bằng Streamlit, GitHub và OpenAI API.

## Chạy trên máy tính

1. Cài Python 3.10+.
2. `pip install -r requirements.txt`
3. Sao chép `.streamlit/secrets.toml.example` thành `.streamlit/secrets.toml`, thay API key của bạn.
4. `streamlit run app.py`

Không commit `secrets.toml` lên GitHub.

## Triển khai Streamlit Community Cloud

1. Tạo repository GitHub mới, tải các file dự án lên (giữ nguyên thư mục).
2. Trong Streamlit Community Cloud, chọn **Create app** và repository vừa tạo, file chạy `app.py`.
3. Vào **App settings → Secrets**, nhập:
   ```
   OPENAI_API_KEY = "sk-..."
   OPENAI_MODEL = "gpt-4o-mini"
   ```
4. Lưu và khởi động lại ứng dụng.

Có thể chạy giao diện, tra cứu bài học mà không cần API key. AI chỉ hoạt động khi có khóa hợp lệ.

## Nội dung và giới hạn

- Nội dung mẫu được biên soạn độc lập; không sao chép MRI Master.
- Bài học ở `data/articles.json`. Thêm bài mới bằng cách chỉnh file JSON, gửi pull request và triển khai lại.
- Trợ lý AI sử dụng bài viết được chọn làm ngữ cảnh, **chưa phải RAG/pgvector**. Không dùng để đưa quyết định lâm sàng.
- Chưa có đăng nhập/quản trị, thống kê, hoặc cơ chế giới hạn chi phí theo người dùng. Trước khi công khai rộng rãi cần thêm xác thực, rate limiting, kiểm duyệt nội dung và giám sát chi phí.
- Không nhập thông tin định danh bệnh nhân hoặc dữ liệu sức khỏe nhạy cảm.
