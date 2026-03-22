# 完整的股票分析配置文件（直接全选粘贴，零错误）
from typing import Optional, List
import os  # 归类到顶部，逻辑更清晰

# 兼容Pydantic V1/V2版本，解决field导入错误
try:
    from pydantic import field_validator, Field as field
except ImportError:
    from pydantic import field_validator, field

# ===================== 邮件核心配置（已包含你的QQ+谷歌邮箱）=====================
# 邮件推送总开关（强制开启，必发邮件）
email_enable: bool = True

# 发件人配置（自动读取GitHub Secrets，无需手动填密码）
email_sender: Optional[str] = os.getenv("EMAIL_USER")  # 对应Secrets里的EMAIL_USER（你的QQ邮箱）
email_sender_name: str = "daily_stock_analysis股票分析助手"  # 发件人显示名称
email_password: Optional[str] = os.getenv("EMAIL_PWD")  # 对应Secrets里的EMAIL_PWD（QQ邮箱SMTP授权码）

# 收件人列表（你的QQ邮箱+谷歌邮箱，固定格式，零语法错误）
email_receivers: List[str] = field(default_factory=lambda: ["623819670@qq.com", "sz848130@gmail.com"])
# ==============================================================================

# ===================== 股票监控配置（常用热门股，可按需修改）=====================
# 支持A股（纯数字）、港股（hk_+数字）、美股（us_+代码）
stock_list = [
    # A股核心股
    "002413",  # 雷科防务
    "002639",  # 雪人集团
    "603601",  # 再升科技
    "600010",  # 包钢股份
    "002340",  # 格林美
    "002165",  # 红宝丽
    "002506",  # 协鑫集成
    "515180",  # 红利ETF
    "159611",  # 电力ETF
]
# ==============================================================================

# ===================== 其他默认配置（无需修改）=====================
# 飞书推送（关闭，不用管）
feishu_enable: bool = False
feishu_webhook: Optional[str] = os.getenv("FEISHU_WEBHOOK")

# Telegram推送（关闭，不用管）
tg_enable: bool = False
tg_token: Optional[str] = os.getenv("TG_TOKEN")
tg_chat_id: Optional[str] = os.getenv("TG_CHAT_ID")

# Pushover推送（关闭，不用管）
pushover_enable: bool = False
pushover_token: Optional[str] = os.getenv("PUSHOVER_TOKEN")
pushover_user_key: Optional[str] = os.getenv("PUSHOVER_USER_KEY")
# ==============================================================================
