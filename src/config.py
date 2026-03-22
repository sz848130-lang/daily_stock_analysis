import os
from typing import Optional, List, Dict

# 如果项目确实需要 pydantic，再按需导入；否则可以完全移除
# 这里假设 Config 不需要 pydantic 验证，直接使用普通属性

def setup_env():
    """加载环境变量到os.environ，用于GitHub Actions运行"""
    pass

def get_config():
    """获取全局配置实例（单例）"""
    global _config
    if _config is None:
        _config = Config()
    return _config

_config = None

# 解决 ImportError 的核心变量
extra_litellm_params: Dict = {}   # 如需具体配置，可补充内容

class Config:
    # 邮件推送总开关（强制开启）
    email_enable: bool = True

    # 发件人配置
    email_sender: Optional[str] = os.getenv("EMAIL_USER")          # 你的QQ邮箱
    email_sender_name: str = "daily_stock_analysis股票分析助手"
    email_password: Optional[str] = os.getenv("EMAIL_PWD")         # QQ邮箱SMTP授权码

    # 收件人列表（直接使用列表，不使用 pydantic field）
    email_receivers: List[str] = ["623819670@qq.com", "sz848130@gmail.com"]

    # 股票/ETF列表
    stock_list = [
        "002413", "002639", "603601", "600010", "002340",
        "002165", "002506", "515180", "159611",
    ]

    # LLM 相关配置
    llm_model: str = "gemini-1.5-flash"
    llm_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")

    # 其他推送（默认关闭）
    feishu_enable: bool = False
    feishu_webhook: Optional[str] = os.getenv("FEISHU_WEBHOOK")
    tg_enable: bool = False
    tg_token: Optional[str] = os.getenv("TG_TOKEN")
    tg_chat_id: Optional[str] = os.getenv("TG_CHAT_ID")
    pushover_enable: bool = False
    pushover_token: Optional[str] = os.getenv("PUSHOVER_TOKEN")
    pushover_user_key: Optional[str] = os.getenv("PUSHOVER_USER_KEY")
