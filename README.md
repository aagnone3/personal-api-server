# personal-api-server

## Investing

### Crypto
Environment variables needed:
- `COINBASE_API_PASSPHRASE`
- `COINBASE_API_KEY`
- `COINBASE_API_SECRET`

`/portfolio`: the current status of my BTC portfolio

## Deployment
```bash
cd _deploy_
./deploy.sh <host> <directory>
    <host>: deployment server host
    <directory>: relative directory for deployment files (from home directory)
```