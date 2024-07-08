# 

<div align="center">
  <h2><b> Shuishui </b></h2>
</div>


![PRs Welcome](https://img.shields.io/badge/PRs-Welcome-green) 
[![Visits Badge](https://badges.pufler.dev/visits/ztxtech/shuishui)](https://github.com/ztxtech/shuishui)
[![GitHub last commit](https://img.shields.io/github/last-commit/ztxtech/shuishui)](https://github.com/ztxtech/shuishui/activity?ref=master&activity_type=direct_push)
[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/ztxtech/shuishui)](https://github.com/ztxtech/shuishui/graphs/commit-activity)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/ztxtech/shuishui)](https://github.com/ztxtech/shuishui)
[![GitHub](https://img.shields.io/github/license/ztxtech/shuishui)](https://github.com/ztxtech/shuishui/blob/main/LICENSE)
[![Docker Pulls](https://img.shields.io/docker/pulls/ztxtechnology/shuishui)](https://hub.docker.com/r/ztxtechnology/shuishui)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/ztxtechnology/shuishui/0.0.1-amd64)](https://hub.docker.com/r/ztxtechnology/shuishui)
[![GitHub Repo stars](https://img.shields.io/github/stars/ztxtech/shuishui)](https://github.com/ztxtech/shuishui)
[![GitHub forks](https://img.shields.io/github/forks/ztxtech/shuishui)](https://github.com/ztxtech/shuishui)
[![GitHub watchers](https://img.shields.io/github/watchers/ztxtech/shuishui)](https://github.com/ztxtech/shuishui)

### A hangout script for the BBS of University of Electronic Science and Technology of China (UESTC). This script automates the process of keeping your account active on the UESTC BBS.

## Usage

Run the following command to start the container with your credentials:

```bash
docker run -d --name {container_name} -e NAME={username} -e PASSWORD={password} ztxtechnology/shuishui:0.0.1-amd64
```

For ARM64 architecture:

```bash
docker run -d --name {container_name} -e NAME={username} -e PASSWORD={password} ztxtechnology/shuishui:0.0.1-arm64
```

## Requirements

- Python >=3.7
- lxml
- requests
- urllib3

## Acknowledgements

This project was inspired by and borrows code from [OnHook](https://github.com/Colouredseal/OnHook) by [Colouredseal](https://github.com/Colouredseal). Many thanks for the initial groundwork that made this project possible.
