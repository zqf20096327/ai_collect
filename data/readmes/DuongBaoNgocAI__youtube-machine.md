# YouTube Machine

**Quy trình xây kênh YouTube từ số 0 đến video đăng được, chạy bằng trợ lý AI trên máy bạn.**

Phiên bản 1.1.0 · Phát hành bởi AI CỘNG VN · [English](README.en.md)

YouTube Machine là bộ 28 skill cho trợ lý AI chạy trên máy, dùng tốt nhất với Claude Code. Bộ skill dẫn bạn đi qua từng bước, từ lúc chọn chủ đề kênh tới khi đăng video và học từ số liệu thật. Ở mỗi bước, trợ lý hỏi bạn vài câu trước khi làm, nên kênh mang dấu ấn riêng của bạn. Mọi kết quả được lưu trong thư mục hồ sơ kênh, nên bạn làm tiếp lúc nào cũng được.

> Nội dung skill nằm trên máy chủ và được phát qua **Cổng YTM**. Repo này chỉ có phần khung, công cụ và mẫu. Muốn dùng, bạn đăng nhập bằng Gmail đã đăng ký YouTube Machine.

---

## Tính năng

### Xây kênh, làm một lần

| Bước | Việc | Skill |
|---|---|---|
| 0 | Dò cấu hình máy, đề xuất dựng bằng Blender hay CapCut | `youtube-machine` |
| 1 | Chọn ngách và khán giả, chấm điểm từng phương án | `yt-01-niche` |
| 2 | Nghiên cứu 5–10 kênh đối thủ, tìm công thức đang hiệu quả và chỗ còn trống | `yt-02-competitor-research` |
| 3 | Từ khóa và chủ đề đang lên (gợi ý tìm kiếm, Google Trends, tiêu đề top) | `yt-03-keyword-research` |
| 4 | Bộ thương hiệu: tên kênh, handle, mô tả SEO, tag, giọng điệu, bảng màu | `yt-04-brand` |
| 4b | Phong cách hình ảnh cố định, khóa phong cách, quy tắc nhân vật, ảnh thử | `yt-04b-visual-style` |
| 5 | Checklist tạo và cài đặt kênh, kèm nội dung để dán sẵn | `yt-05-channel-setup` |
| 6 | 30 ý tưởng video đầu và lịch đăng 8–12 tuần | `yt-06-content-plan` |
| 6b | Rà chính sách, bản quyền nhạc và hình, khai báo nội dung AI | `yt-06b-policy-check` |

### Làm từng video, lặp lại

| Bước | Việc | Skill |
|---|---|---|
| 6c | Kiểm tra nhu cầu, chốt tiêu đề và thumbnail trước khi viết | `yt-06c-demand-check` |
| 7 | Kịch bản giữ chân người xem và file lời đọc liền mạch | `yt-07-script` |
| 7b | Giọng đọc AI (ElevenLabs), phụ đề SRT đã sửa chữ, mốc chương | `yt-07b-voice-srt` |
| 7c | Mỗi dòng SRT là một cảnh, có prompt hình và nhân vật đồng nhất | `yt-07c-shotlist` |
| 7d | Kế hoạch dựng giữ chân: nhịp, cú lật, nhạc theo chặng | `yt-07d-edit-plan` |
| 7e | Dựng video thật bằng Blender (tự động) hoặc CapCut (làm tay) | `yt-07e-render` |
| 7m | Motion graphics: chữ động, bản đồ, dòng thời gian, đếm số, sơ đồ | `yt-07m-motion` |
| Quay | Kế hoạch quay, chữ nhắc, cảnh phụ cho video quay thật | `yt-07q-quay` |
| Cắt | Cắt theo lời: bỏ câu hỏng, khoảng lặng, từ đệm | `yt-07f-cat-theo-chu` |
| Soát | Soát kỹ thuật và đối chiếu lời hứa của video trước khi đăng | `yt-07x-soat` |
| Shorts | Chọn đoạn đứng độc lập, cắt dọc, thêm phụ đề | `yt-07r-shorts` |
| 7k | Shorts dọc 3D tự dựng, 10 phong cách (khối pixel, đất sét, giấy gấp, len nỉ...), không tốn tín dụng hình | `yt-07k-khoi-vuong` |
| Thumbnail | Ghép chữ đúng dấu tiếng Việt, so ở cỡ nhỏ | `yt-08t-thumbnail` |
| 8 | Gói SEO: 5 tiêu đề, mô tả, chương, tag, checklist đăng | `yt-08-seo-publish` |
| 9 | 48 giờ đầu sau khi đăng, xử lý khi video ít lượt xem | `yt-09-post-publish` |
| 10 | Học từ số liệu thật và đổi cách làm cho video sau | `yt-10-learning` |

### Skill hỗ trợ

| Skill | Việc |
|---|---|
| `yt-00-folders` | Tạo, kiểm tra, dọn thư mục kênh và video; báo dung lượng |
| `yt-osint` | Tra nguồn mở, kiểm chứng tuyên bố, tìm tư liệu gốc cho video |
| `yt-mo-xe-dung` | Mổ xẻ cách đối thủ dựng: nhịp cắt, chữ trên hình, tiếng động. Chỉ cần đưa link |

### Điểm khác biệt

- **Hỏi trước khi làm.** Mỗi bước mở đầu bằng 2–5 câu hỏi có ảnh hưởng tới kết quả, kèm đề xuất. Câu nào trợ lý đã biết câu trả lời thì bỏ qua.
- **Kiểm tra nhu cầu trước khi bỏ công.** Chưa viết kịch bản khi chưa có tiêu đề và thumbnail đáng bấm, và chưa có bằng chứng rằng có người xem chủ đề đó.
- **Không lặp khuôn.** Có 16 công thức định dạng (lời trước, cảnh trước, quay trước, màn hình, nhạc, dữ liệu, tư liệu sẵn…). Mỗi video qua năm cổng giá trị. Lệnh `node tools/chong-lap.mjs` so kịch bản mới với các video trước.
- **Kênh tự học.** Số liệu thật được ghi vào `learnings.md`, và mọi bước sau đọc file này trước khi làm.
- **Báo cáo trực quan.** Ở mỗi chỗ cần bạn quyết định, trợ lý xuất một trang HTML ngắn có thẻ lựa chọn và bảng dữ liệu.
- **Nhiều kênh.** Mỗi kênh có một thư mục riêng trong `channels/`, và trợ lý nhớ mỗi kênh đang ở bước nào.

---

## Yêu cầu

- Windows 10 hoặc 11. macOS và Linux chạy được một phần.
- [Node.js](https://nodejs.org) bản LTS.
- Claude Code, hoặc app Claude cho máy tính (tab Code). Gemini CLI, Google Antigravity và Codex đọc được bộ skill, nhưng cách nối Cổng YTM cho các trợ lý này sẽ có ở bản sau.
- Kết nối mạng và Gmail đã đăng ký YouTube Machine.
- Ổ đĩa còn trống nhiều. Mỗi video thường chiếm 1–4 GB.

## Cài đặt

**Cách 1: dùng git**

```powershell
git clone https://github.com/DuongBaoNgocAI/youtube-machine.git D:\YoutubeMachine
```

**Cách 2: tải file zip.** Bấm **Code → Download ZIP** trên trang này, rồi giải nén vào một thư mục có đường dẫn ngắn, không dấu, ví dụ `D:\YoutubeMachine`.

Sau đó mở thư mục này trong trợ lý AI:

| Trợ lý | Cách mở |
|---|---|
| Claude Code / app Claude (tab Code) | Chọn thư mục làm thư mục làm việc. Khi được hỏi có dùng máy chủ MCP `ytm` không, chọn đồng ý |
| Google Antigravity | File → Open Folder |
| Codex | Mở thư mục |
| Gemini CLI | Mở PowerShell tại thư mục, chạy `gemini` |

Claude không hỏi về máy chủ `ytm` thì chạy lệnh sau tại thư mục, rồi mở lại Claude:

```powershell
claude mcp add ytm -- node tools/ytm-cong.mjs
```

### Lỗi thường gặp

| Bạn thấy | Làm gì |
|---|---|
| `node` is not recognized | Cài lại Node.js bản LTS rồi khởi động lại máy |
| Trợ lý không biết quy trình YouTube Machine | Kiểm tra đã mở đúng thư mục có file `AGENTS.md`, rồi mở phiên mới |
| Trợ lý không thấy công cụ `ytm_...` | Chạy lệnh `claude mcp add ytm` ở trên rồi mở lại Claude |
| Trợ lý báo không chạy được lệnh | Đổi sang chế độ cho phép chạy lệnh |
| Báo chưa có ffmpeg | Chạy `winget install Gyan.FFmpeg`, đóng và mở lại trợ lý |

Vẫn chưa xong thì gửi ảnh chụp lỗi và tên trợ lý bạn dùng vào nhóm hỗ trợ. Đừng gửi mật khẩu hay khóa API lên nhóm.

## Cách dùng

Mở trợ lý trong thư mục và nói bằng lời thường:

| Bạn nói | Trợ lý làm |
|---|---|
| "Tôi muốn xây kênh YouTube mới" | Dò máy, hỏi vài câu, rồi dẫn bạn từ bước 1 |
| "Tiếp tục kênh <tên>" | Đọc tiến độ và làm bước kế tiếp |
| "Viết kịch bản video số 4 cho kênh <tên>" | Đi thẳng tới bước đó |
| "Làm motion cho đoạn này" | Dựng motion graphics bằng HyperFrames |
| "Phân tích cách dựng video <link>" | Mổ xẻ nhịp cắt và cấu trúc của video đó |
| "Kênh chiếm bao nhiêu ổ đĩa" / "Dọn file video 003" | Báo dung lượng, liệt kê file rồi chờ bạn đồng ý mới dọn |

**Lần đầu trên mỗi máy**, trợ lý mở trình duyệt tới trang chọn tài khoản Google. Bạn chọn Gmail đã đăng ký, thấy trình duyệt báo "Đã đăng nhập" thì quay lại trợ lý. Bạn không phải nhập mã nào, và trợ lý không thấy mật khẩu của bạn. Mỗi tài khoản dùng được trên 2 máy. Muốn đổi máy thì gỡ máy cũ ở trang YouTube Machine.

Cũng trong lần đầu, trợ lý hỏi bạn muốn chế độ **người mới** (giải thích kỹ, hỏi từng câu) hay **nhanh** (gom câu hỏi lại, không giải thích). Lựa chọn này được lưu lại.

## Công cụ đi kèm quy trình

Không cần cài hết ngay. Tới bước nào cần công cụ gì, trợ lý sẽ báo.

| Công cụ | Dùng để |
|---|---|
| ElevenLabs hoặc công cụ giọng khác | Tạo giọng đọc và phụ đề SRT |
| [Flow AIC](https://github.com/DuongBaoNgocAI/flow-aic-releases/releases/latest) | Tạo ảnh và clip hàng loạt. Không có thì skill đưa prompt để bạn dùng công cụ khác |
| Blender 5.x + ffmpeg | Đường dựng tự động |
| CapCut | Đường dựng làm tay, hợp với máy yếu |
| HyperFrames + ffmpeg | Motion graphics, tự tải qua `npx` khi dùng |

Chạy `node tools/do-may.mjs` để xem máy bạn hợp với đường dựng Blender hay CapCut.

## Cấu trúc thư mục

```
youtube-machine/
├── AGENTS.md, GEMINI.md      # luật cho trợ lý AI
├── .mcp.json                 # khai báo Cổng YTM cho Claude Code
├── .claude/skills/           # skill giữ chỗ, nội dung lấy qua Cổng YTM
├── .agents/, .agent/         # bản cho trợ lý khác
├── tools/
│   ├── ytm-cong.mjs          # Cổng YTM: đăng nhập Google, đọc skill
│   ├── do-may.mjs            # dò máy, đề xuất đường dựng
│   ├── kenh.mjs              # tạo kênh, tạo video, kiểm tra, dọn
│   ├── chong-lap.mjs         # so kịch bản với video trước
│   ├── soat.mjs              # soát thành phẩm
│   ├── flow/ motion/ footage/ thumbnail/ blender/
└── channels/
    ├── _template/            # mẫu hồ sơ kênh
    └── <ten-kenh>/           # hồ sơ kênh của bạn (không đưa lên git)
        └── videos/NNN-slug/  # 1-kich-ban, 2-giong, 3-hinh, 4-dung, 5-xuat, 6-dang
```

Dữ liệu kênh trong `channels/` đã nằm trong `.gitignore`, nên không bị đưa lên GitHub.

## Cập nhật

Khi có bản mới, trợ lý báo ngay đầu phiên. Bạn chỉ cần nói với trợ lý: "cập nhật YouTube Machine".

- Trợ lý chạy `node tools/cap-nhat.mjs`, tải đúng bản tài khoản của bạn được dùng, rồi thay các file của bộ skill. Thư mục `channels/` và hồ sơ kênh giữ nguyên.
- File cũ bị thay được chuyển vào `_thung-rac/cap-nhat-<bản cũ>-sang-<bản mới>-<giờ>/`. Bạn tự xóa khi không cần nữa.
- Đã tự tải file zip ở trang YouTube Machine thì nói: "cập nhật YouTube Machine từ file zip <đường dẫn>".
- Gói 1.0.0 chưa có lệnh này. Lần đầu lên bản mới, tải zip ở mục Tải về rồi chép đè vào thư mục đang dùng. Từ đó trở đi chỉ cần nói với trợ lý.

Cập nhật xong, trợ lý báo bạn đang ở bản nào và bản đó có gì mới. Danh sách thay đổi ở [CHANGELOG.md](CHANGELOG.md).

## Nguyên tắc

- Trò chuyện với bạn bằng tiếng Việt. Nội dung cho khán giả viết bằng ngôn ngữ của kênh.
- Không bịa số liệu. Thứ gì chưa kiểm chứng được thì ghi "chưa kiểm chứng". Không hứa lượt xem.
- Việc cần tài khoản Google (tạo Gmail, tạo kênh, đăng video) là bạn tự làm. Trợ lý chỉ đưa checklist và nội dung để dán.
- Không xóa hẳn file của bạn. Khi dọn, file được chuyển vào `_thung-rac/`.

## Hỗ trợ

Nhóm Zalo: https://zalo.me/g/yenkqg494

Điều khoản sử dụng ở [LICENSE.txt](LICENSE.txt).
