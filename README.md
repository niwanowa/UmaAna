# UmaAna
ウマ娘プリティーダービー(For Windows)のレスポンスを解析して良い感じに表示する。


## 前提
- [EXNOA-CarrotJuicer](https://github.com/CNA-Bld/EXNOA-CarrotJuicer)を導入していること。
- EXNOA-CarrotJuicerと同階層にcjconfig.jsonを配置していること。
- cjconfig.jsonでの設定内に以下を記載していること。
```json
    "enable_notifier": true,
    "notifier_host": "http://127.0.0.1:4693",
```

### cjconfig.json例
```json
{
	"save_request": true,
	"save_response": true,

	"enable_ansi_colors": true, 

	"enable_notifier": true,
	"notifier_host": "http://127.0.0.1:4693",
	"notifier_connection_timeout_msec": 100,
	"notifier_print_error": true,

	"aoharu_team_sort_with_speed": true,
	"aoharu_print_team_average_status_max_turn": 0,

	"climax_print_shop_items": true
}
```

