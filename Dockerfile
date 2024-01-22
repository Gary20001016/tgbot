# 使用官方Python运行时作为父镜像
FROM python:3.8

# 设置工作目录
WORKDIR /app

# 将当前目录内容复制到位于/app中的容器中
COPY . /app

# 安装requirements.txt中指定的任何所需包
RUN pip install aiohttp==3.9.1 \
                aiosignal==1.3.1 \
                anyio==4.2.0 \
                APScheduler==3.6.3 \
                async-timeout==4.0.3 \
                attrs==23.2.0 \
                base58==2.1.1 \
                bitarray==2.9.2 \
                cachetools==4.2.2 \
                certifi==2023.11.17 \
                charset-normalizer==3.3.2 \
                cytoolz==0.12.2 \
                eth-abi==2.2.0 \
                eth-account==0.5.9 \
                eth-hash==0.6.0 \
                eth-keyfile==0.5.1 \
                eth-keys==0.3.4 \
                eth-rlp==0.2.1 \
                eth-typing==2.3.0 \
                eth-utils==1.9.5 \
                exceptiongroup==1.2.0 \
                frozenlist==1.4.1 \
                h11==0.14.0 \
                hexbytes==0.3.1 \
                httpcore==1.0.2 \
                httpx==0.25.2 \
                idna==3.6 \
                ipfshttpclient==0.8.0a2 \
                jsonschema==4.21.0 \
                jsonschema-specifications==2023.12.1 \
                lru-dict==1.3.0 \
                multiaddr==0.0.9 \
                multidict==6.0.4 \
                netaddr==0.10.1 \
                parsimonious==0.8.1 \
                protobuf==3.19.5 \
                pycryptodome==3.20.0 \
                python-dotenv==1.0.0 \
                python-telegram-bot==13.15 \
                pytz==2023.3.post1 \
                referencing==0.32.1 \
                requests==2.31.0 \
                rlp==2.0.1 \
                rpds-py==0.17.1 \
                six==1.16.0 \
                sniffio==1.3.0 \
                toolz==0.12.0 \
                tornado==6.1 \
                typing_extensions==4.9.0 \
                tzlocal==5.2 \
                urllib3==2.1.0 \
                varint==1.0.2 \
                web3==5.31.4 \
                websockets==9.1 \
                yarl==1.9.4

# 在容器启动时运行tgbot.py
CMD ["python", "tgbot.py"]
