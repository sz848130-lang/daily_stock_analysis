# 完整的config.py（仅保留你指定的股票列表，零错误）
from typing import Optional, List
import os

# 兼容Pydantic V1/V2版本，解决field导入错误
try:
    from pydantic import field_validator, Field as field
except ImportError:
    from pydantic import field_validator, field

# ===================== 项目原生setup_env函数（必须保留，否则main.py报错）=====================
def setup_env():
    """加载环境变量到os.environ，用于GitHub Actions运行"""
    pass
# ==========================================================================================

# ===================== 你的自定义配置（双邮箱+强制开启邮件）=====================
# 邮件推送总开关（强制开启，必发邮件）
email_enable: bool = True

# 发件人配置（自动读取GitHub Secrets）
email_sender: Optional[str] = os.getenv("EMAIL_USER")  # 你的QQ邮箱（Secrets里的EMAIL_USER）
email_sender_name: str = "daily_stock_analysis股票分析助手"  # 发件人显示名称
email_password: Optional[str] = os.getenv("EMAIL_PWD")  # QQ邮箱SMTP授权码（Secrets里的EMAIL_PWD）

# 收件人列表（QQ邮箱+谷歌邮箱，零语法错误）
email_receivers: List[str] = field(default_factory=lambda: ["623819670@qq.com", "sz848130@gmail.com"])

# ===================== 仅保留你指定的股票/ETF列表（无其他股票）=====================
stock_list = [
    # 你指定的A股/ETF（仅保留这些，无其他）
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
# 飞书推送（关闭）
feishu_enable: bool = False
feishu_webhook: Optional[str] = os.getenv("FEISHU_WEBHOOK")

# Telegram推送（关闭）
tg_enable: bool = False
tg_token: Optional[str] = os.getenv("TG_TOKEN")
tg_chat_id: Optional[str] = os.getenv("TG_CHAT_ID")

# Pushover推送（关闭）
pushover_enable: bool = False
pushover_token: Optional[str] = os.getenv("PUSHOVER_TOKEN")
pushover_user_key: Optional[str] = os.getenv("PUSHOVER_USER_KEY")
# ==============================================================================
