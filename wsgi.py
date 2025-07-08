from app.like_routes import initialize_routes
from app.token_manager import TokenCache
from config import CONFIG

app = Flask(__name__)

# 🔧 Load server configs manually (for safety)
from app.like_routes import load_server_configs
servers_config = load_server_configs()

# 🔐 Token Cache
token_cache = TokenCache(servers_config)

# 🔁 Initialize API Routes
initialize_routes(app, servers_config, token_cache)
