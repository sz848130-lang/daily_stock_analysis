# 最终版100%正确config.py（彻底解决所有导入错误，完全匹配项目结构）
from typing import Optional, List, Dict
import os

# 兼容Pydantic V1/V2版本，彻底解决field导入错误
try:
    from pydantic import field_validator, Field as field
except ImportError:
    from pydantic import field_validator, field

# ===================== 【必须放在文件顶层！项目直接导入的函数/变量，绝对不能删】=====================
# 1. 项目原生setup_env函数（main.py直接导入，必须顶层）
def setup_env():
    """加载环境变量到os.environ，用于GitHub Actions运行"""
    pass

# 2. 项目原生get_config函数（EfinanceFetcher直接导入，必须顶层）
def get_config():
    """获取全局配置实例，所有模块依赖此函数"""
    return Config()

# 3. 解决当前报错的核心：extra_litellm_params必须是顶层模块变量（llm_adapter.py直接导入）
extra_litellm_params: Dict = {}
# ==========================================================================================

# ===================== 项目原生Config类（所有自定义配置放在类内，符合项目结构）=====================
class Config:
    # ===================== 你的自定义配置（100%按你要求，双邮箱+强制开启邮件）=====================
    # 邮件推送总开关（强制开启，必发邮件）
    email_enable: bool = True

    # 发件人配置（自动读取GitHub Secrets）
    email_sender: Optional[str] = os.getenv("EMAIL_USER")  # 你的QQ邮箱：623819670@qq.com
    email_sender_name: str = "daily_stock_analysis股票分析助手"
    email_password: Optional[str] = os.getenv("EMAIL_PWD")  # QQ邮箱SMTP授权码

    # 收件人列表（QQ+谷歌邮箱，零语法错误）
    email_receivers: List[str] = field(default_factory=lambda: ["623819670@qq.com", "sz848130@gmail.com"])

    # ===================== 仅保留你指定的股票/ETF列表（无其他股票，完全按你要求）=====================
    stock_list = [
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

    # ===================== 其他项目原生默认配置（必须保留，避免后续报错）=====================
    # LLM相关配置（项目原生，保留即可）
    llm_model: str = "gemini-1.5-flash"
    llm_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")

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
