# Sentrysk MacOS Agent

| Content  | 
| ------------- |
| [Project Architecture](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/README.md#architecture)     | 
| [Requirements](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/README.md#requirements) |
| [How to Install](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/README.md#how-to-install)   | 
| [Roadmap](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/README.md#roadmap)   | 
| [Modules](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/README.md#modules)    | 

## Architecture

## Requirements
| Program  | Version |
| ------------- |:-------------:|
| Python      | 3.10     |

## How To Install

- Install requirements
```
pip install -r requirements.txt
```
Note: **Admin rights needed** 

- Run the app
```
python3 agent.py
```
Note: **Admin rights needed** 

## Roadmap
### Version 1.0-Beta
- [x] [Developing NPM data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/1)
- [x] [Developing Pip data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/2)
- [x] [Developing installed apps data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/3)
- [x] [Developing last logons data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/4)
- [x] [Developing services data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/5)
- [x] [Developing users data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/6)
- [x] [Developing system information data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/7)
- [ ] [Developing docker data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/8)
- [x] [Developing config file](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/9)
- [x] [Developing data sender functions](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/10)
- [x] [Developing scheduled jobs](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/11)
- [ ] [Developing config sender module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/issues/12)

### Feature Development
- [ ] Process data collector module
- [ ] Memory data collector module (planning to keep 1 month data)
- [ ] CPU data collector module (planning to keep 1 month data)



## Modules
- [NPM data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/npm_info.py)
- [Pip data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/pip_info.py)
- [installed apps data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/installed_apps.py)
- [last logons data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/last_logon.py)
- [services data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/service_info.py)
- [users data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/user_info.py)
- [system information data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/system_info.py)
- [docker data collector module](https://github.com/sentrysk/Sentrysk-MacOS-Agent/blob/main/Modules/docker_info.py)
