import os
from typing import Optional, List, Dict

# ===================== 顶层函数/变量 =====================
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

def get_api_keys_for_model(model_name: str) -> Optional[str]:
    """根据模型名称返回对应的 API 密钥（用于 lm_adapter）"""
    if model_name.startswith("gemini"):
        return os.getenv("GEMINI_API_KEY")
    # 如需其他模型，在此添加
    return None

# 解决之前报错的变量
extra_litellm_params: Dict = {}   # 如需具体配置，可添加内容，例如 {"thinking": True}

# ===================== Config 类 =====================
class Config:
    # 邮件推送总开关
    email_enable: bool = True

    # 发件人配置
    email_sender: Optional[str] = os.getenv("EMAIL_USER")
    email_sender_name: str = "daily_stock_analysis股票分析助手"
    email_password: Optional[str] = os.getenv("EMAIL_PWD")

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
