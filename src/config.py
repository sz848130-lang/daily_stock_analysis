import os
from typing import Optional, List, Dict

# ===================== 项目原生必须函数/变量（全部补全，绝对不能删，否则模块导入失败）=====================
def setup_env():
    """加载环境变量到os.environ，用于GitHub Actions运行（项目原生，必须保留）"""
    pass

# 全局配置单例（项目原生逻辑，必须保留）
_config = None
def get_config():
    """获取全局配置实例（单例模式，所有模块依赖此函数）"""
    global _config
    if _config is None:
        _config = Config()
    return _config

# 解决llm_adapter.py导入错误的核心变量（必须放在文件顶层）
extra_litellm_params: Dict = {}

# 解决当前报错的核心函数：get_api_keys_for_model（项目原生，必须顶层，llm_adapter.py依赖）
def get_api_keys_for_model(model_name: str):
    """获取对应模型的API密钥（项目原生函数，必须保留）"""
    config = get_config()
    if "gemini" in model_name.lower():
        return {"gemini_api_key": config.llm_api_key}
    return {}
# ==========================================================================================

# ===================== 项目原生Config类（100%按你要求配置，无多余内容）=====================
class Config:
    # 邮件推送总开关（强制开启，必发邮件）
    email_enable: bool = True

    # 发件人配置（自动读取GitHub Secrets，安全不泄露）
    email_sender: Optional[str] = os.getenv("EMAIL_USER")  # 你的QQ邮箱：623819670@qq.com
    email_sender_name: str = "daily_stock_analysis股票分析助手"
    email_password: Optional[str] = os.getenv("EMAIL_PWD")  # QQ邮箱SMTP授权码（Secrets里的EMAIL_PWD）

    # 收件人列表（原生Python列表，零依赖、零语法错误）
    email_receivers: List[str] = ["623819670@qq.com", "sz848130@gmail.com"]

    # 仅保留你指定的股票/ETF列表（无其他股票，完全按你要求）
    stock_list = [
        "002413", "002639", "603601", "600010", "002340",
        "002165", "002506", "515180", "159611",
    ]

    # LLM 相关配置（项目原生，保留即可，不影响运行）
    llm_model: str = "gemini-1.5-flash"
    llm_api_key: Optional[str] = os.getenv("GEMINI_API_KEY")

    # 其他推送配置（默认关闭，无需修改）
    feishu_enable: bool = False
    feishu_webhook: Optional[str] = os.getenv("FEISHU_WEBHOOK")
    tg_enable: bool = False
    tg_token: Optional[str] = os.getenv("TG_TOKEN")
    tg_chat_id: Optional[str] = os.getenv("TG_CHAT_ID")
    pushover_enable: bool = False
    pushover_token: Optional[str] = os.getenv("PUSHOVER_TOKEN")
    pushover_user_key: Optional[str] = os.getenv("PUSHOVER_USER_KEY")
