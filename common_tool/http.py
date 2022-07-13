import json
import re

RE_MOBILE = re.compile(r"(iphone|ipod|blackberry|android|palm|windows\s+ce|windows\s+phone)", re.I)
RE_DESKTOP = re.compile(r"(windows|linux|os\s+[x9]|solaris|bsd)", re.I)
RE_BOT = re.compile(r"(spider|crawl|slurp)", re.I)


def get_post_data(request):
    """
    获取request的post_data
    """
    try:
        return json.loads(request.body)
    except:
        return {}


def get_ip_from_request(request):
    """
    从request请求中提取访问ip
    """
    if request.META.get('HTTP_X_FORWARDED_FOR'):
        ip = request.META.get("HTTP_X_FORWARDED_FOR")
    else:
        ip = request.META.get("REMOTE_ADDR")
    return ip


def get_start_and_end_by_page(request, page_size=20):
    page = request.GET.get("page", 0)
    start = int(page) * page_size
    return start, start + page_size


def is_desktop_agent(user_agent):
    """
    Anything that looks like a phone isn't a desktop.
    Anything that looks like a desktop probably is.
    Anything that looks like a bot should default to desktop.
    """
    return (not bool(RE_MOBILE.search(user_agent))
            and bool(RE_DESKTOP.search(user_agent))
            or bool(RE_BOT.search(user_agent)))


def get_user_agent(request):
    # Some mobile browsers put the User-Agent in a HTTP-X header
    return (request.META.get('HTTP_X_OPERAMINI_PHONE_UA')
            or request.META.get('HTTP_X_SKYFIRE_PHONE')
            or request.META.get('HTTP_USER_AGENT', ''))
