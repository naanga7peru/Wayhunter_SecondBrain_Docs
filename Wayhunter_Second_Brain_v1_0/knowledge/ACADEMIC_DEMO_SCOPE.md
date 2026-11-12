# Academic Final Project scope guardrail (no feature rewrite)

- The 7-person team is preparing a one-day **academic demonstration**, not an immediately deployed commercial product. User journeys and approved rules remain the source of truth.
- Build/test real end-to-end Flutter → ASP.NET API → SQL Server → Angular Admin → Flutter for the core demonstrated flows, not just static screenshots. Actual development has **not started** according to the project owner.
- Demo vouchers use **sample image, unique demo code, QR**, Coins ledger and Admin approval; **no real cash transfer, purchased voucher, merchant settlement** is needed to demonstrate the agreed business flow.
- Admin Voucher Photo/PDF & manual validation remain documented; OCR/barcode **intake** is optional (QR *issuance/display* is required for demo voucher).
- 118 proposed ERD tables are a reference design, **not a requirement to create 118 SQL tables for the demo**. Plan an MVP subset consistent with the workflows when implementation begins.
- Demo does not waive privacy, unique winner, Coins idempotency, proper statuses or manual Admin approval. No production KPI, cost or uptime promises are inferred from a demo.
- Developer may simulate external integrations only when clearly labelled as demo and **not** substitute mock balances/approvals for the core backend/database evidence that the project aims to demonstrate.
