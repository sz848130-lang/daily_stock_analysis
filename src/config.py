import os
from typing import Optional, List, Dict

# ===================== 顶层函数/变量（修正函数名，匹配项目导入要求）=====================
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
    """根据模型名称返回对应的 API 密钥"""
    if model_name.startswith("gemini"):
        return os.getenv("GEMINI_API_KEY")
    # 其他模型添加在此
    return None

# 关键修正：函数名从 get_configured_lm_models → get_configured_llm_models（补全l）
def get_configured_llm_models() -> List[Dict[str, str]]:
    """返回配置的 LLM 模型列表（匹配项目导入的函数名）"""
    config = get_config()
    # 如果项目只使用一个模型，返回单元素列表
    return [{"model": config.llm_model, "api_key": config.llm_api_key}]

def get_llm_config() -> Dict:
    """返回 LLM 配置字典（兼容可能的使用）"""
    config = get_config()
    return {
        "model": config.llm_model,
        "api_key": config.llm_api_key,
        "temperature": 0.7,
    }

def get_litellm_params() -> Dict:
    """返回 LiteLLM 额外参数"""
    return extra_litellm_params

extra_litellm_params: Dict = {}   # 可根据需要填充，如 {"thinking": True}

# ===================== Config 类（完全保留你的配置）=====================
class Config:
    # 邮件配置
    email_enable: bool = True
    email_sender: Optional[str] = os.getenv("EMAIL_USER")
    email_sender_name: str = "daily_stock_analysis股票分析助手"
    email_password: Optional[str] = os.getenv("EMAIL_PWD")
    email_receivers: List[str] = ["623819670@qq.com", "sz848130@gmail.com"]

    # 股票列表（仅保留你指定的标的）
    stock_list = [
        "002413", "002639", "603601", "600010", "002340",
        "002165", "002506", "515180", "159611",
    ]

    # LLM 配置
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
