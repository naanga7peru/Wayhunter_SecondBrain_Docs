# Decision register — do not infer an answer

| ID | Decision | Current documented status | Affects | Production gate |
|---|---|---|---|---|
| VCH-DEC-01 | Final Coins debit trigger | **RESOLVED 2026-11-11: Admin Approval**, exactly once | BRD, Flutter Wallet, Angular, Backend, ERD, tests | Implement & test |
| VCH-DEC-02 | OCR / QR / barcode extraction now or later? | **PROPOSED / NOT APPROVED** | Admin voucher intake, Backend, optional ERD | Do not implement as required current scope |
| CO-DEC-01 | Coins redemption minimum | **RESOLVED 2026-11-11: >=10,100 spendable to redeem 10,000**, keep >=100 | Wallet, API, tests | Implement & test |
| CO-DEC-02 | Actual cash payout method & settlement/partner terms | **OUT OF ACADEMIC DEMO SCOPE 2026-11-11**; use sample voucher image/code/QR | Redemption, Settlements, Accounting | No actual cash-out |
| GAME-DEC-01 | Winner count | **RESOLVED 2026-11-11: one verified winner per Game** | Game verify, rewards, leaderboard | Implement & test |
| GAME-DEC-02 | Expiry & ongoing attempts | **RESOLVED 2026-11-11, later owner clarification: Admin Approval + 30 days; hide public game, retain Expired/Archived Game record and creator My Games; no playable attempt after expiry** | Game expiry scheduler, creator history | Implement & test |
| SAFETY-DEC-01 | Hazard alerts matching/age | **PARTIALLY RESOLVED 2026-11-11: planned route within 1 km, photo time visible, alert 24h; cooldown unspecified** | Geo alerts/notifications | Implement & test; cooldown is technical config |
| ADMIN-DEC-01 | Exact admin roles and permissions | **DECISION REQUIRED** | Admin authorization & audit | Grant least privilege before production |

Until decisions are signed, maintain a draft note. Once approved, record date, approver, exact wording, affected tests/docs and migration. Never backdate sign-off or invent owner intent.
