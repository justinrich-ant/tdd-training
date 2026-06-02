# flag-service (TDD training demo)

## Running tests
`pytest` — runs the full suite. No build step required.

## Repo layout
- `flag_service/evaluate.py` — core bucketing logic (`is_user_in_rollout`, `evaluate`)
- `flag_service/metrics.py` — rollout analytics helpers (Demo 1)
- `flag_service/rollout_guard.py` — safety guard for prod bumps (Demo 2)
- `flag_service/flags.py` — static flag store (12 flags across dev/staging/prod)
- `tests/` — pytest test suite

## Flag structure
Each flag is a dict:
```
{
  "key": "new-checkout",     # identifier
  "env": "prod",             # dev | staging | prod
  "enabled": True,           # master kill-switch
  "rollout_percent": 25,     # 0-100, fraction of users who see this flag
  "owner": "payments"        # team slug
}
```

## Never
- Never edit a test to make it pass. If a test seems wrong, stop and explain why.
- Write failing tests FIRST. Implementation comes after.
- Never raise a prod flag above its staging rollout_percent.
