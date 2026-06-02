# Static flag store. In a real system this would live in a database.
# 12 flags across dev / staging / prod.

FLAGS = [
    # --- dev: move fast, everything on ---
    {"key": "new-checkout",       "env": "dev",     "enabled": True,  "rollout_percent": 100, "owner": "payments"},
    {"key": "dark-mode",          "env": "dev",     "enabled": True,  "rollout_percent": 100, "owner": "design"},
    {"key": "beta-search",        "env": "dev",     "enabled": True,  "rollout_percent": 100, "owner": "search"},
    {"key": "ai-recommendations", "env": "dev",     "enabled": True,  "rollout_percent": 100, "owner": "ml-platform"},

    # --- staging: graduated rollouts ---
    {"key": "new-checkout",       "env": "staging", "enabled": True,  "rollout_percent": 100, "owner": "payments"},
    {"key": "dark-mode",          "env": "staging", "enabled": True,  "rollout_percent": 50,  "owner": "design"},
    {"key": "beta-search",        "env": "staging", "enabled": True,  "rollout_percent": 25,  "owner": "search"},
    {"key": "ai-recommendations", "env": "staging", "enabled": False, "rollout_percent": 0,   "owner": "ml-platform"},

    # --- prod: conservative ---
    {"key": "dark-mode",          "env": "prod",    "enabled": True,  "rollout_percent": 100, "owner": "design"},
    {"key": "legacy-export",      "env": "prod",    "enabled": True,  "rollout_percent": 50,  "owner": "data"},
    {"key": "new-checkout",       "env": "prod",    "enabled": True,  "rollout_percent": 25,  "owner": "payments"},
    {"key": "beta-search",        "env": "prod",    "enabled": True,  "rollout_percent": 10,  "owner": "search"},
]
