FROM alpine
COPY hello.sh /hello.sh
CMD ["sh", "/hello.sh"]
