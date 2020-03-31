FROM golang:1.14.1-buster as builder

RUN mkdir -p /src
WORKDIR /src
COPY go.* .
RUN go mod download
COPY . .
RUN go build -o scrumpy-backend

FROM alpine
COPY --from=builder /src/scrumpy-backend .
CMD ["./scrumpy-backend"]