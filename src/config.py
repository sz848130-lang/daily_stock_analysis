import os
from typing import Optional, List, Dict

# ===================== 仅保留项目必须的核心函数（无LLM相关）=====================
def setup_env():
    """加载环境变量（项目运行必须）"""
    pass

# 全局单例配置（仅为兼容项目结构）
_config = None
def get_config():
    """获取配置实例（仅保留，无LLM逻辑）"""
    global _config
    if _config is None:
        _config = Config()
    return _config

# ===================== 你的核心配置（只保留股票+邮件，无任何LLM）=====================
class Config:
    # 邮件配置（强制开启，你的双邮箱）
    email_enable: bool = True
    email_sender: Optional[str] = os.getenv("EMAIL_USER")          # 你的QQ邮箱
    email_sender_name: str = "daily_stock_analysis股票分析助手"
    email_password: Optional[str] = os.getenv("EMAIL_PWD")         # QQ邮箱SMTP授权码
    email_receivers: List[str] = ["623819670@qq.com", "sz848130@gmail.com"]

    # 你的股票/ETF列表（仅保留你指定的9只）
    stock_list = [
        "002413", "002639", "603601", "600010", "002340",
        "002165", "002506", "515180", "159611",
    ]

    # 其他推送（默认关闭，无需修改）
    feishu_enable: bool = False
    feishu_webhook: Optional[str] = os.getenv("FEISHU_WEBHOOK")
    tg_enable: bool = False
    tg_token: Optional[str] = os.getenv("TG_TOKEN")
    tg_chat_id: Optional[str] = os.getenv("TG_CHAT_ID")
    pushover_enable: bool = False
    pushover_token: Optional[str] = os.getenv("PUSHOVER_TOKEN")
    pushover_user_key: Optional[str] = os.getenv("PUSHOVER_USER_KEY")
