name: Tweet Scheduler

on:
  workflow_dispatch:
  schedule:
    - cron: '0 */2 * * *'  # Runs every 2 minutes (adjust as needed)

jobs:
  tweet:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.12'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install tweepy
      - name: Run script
        run: python main.py
        env:
          BEARER_TOKEN: ${{ secrets.BEARER_TOKEN }}
          API_KEY: ${{ secrets.API_KEY }}
          API_SECRET_KEY: ${{ secrets.API_SECRET_KEY }}
          ACCESS_TOKEN: ${{ secrets.ACCESS_TOKEN }}
          ACCESS_TOKEN_SECRET: ${{ secrets.ACCESS_TOKEN_SECRET }}
