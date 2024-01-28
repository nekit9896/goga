#!/bin/bash
API_ENDPOINT="http://api.example.com/product_stock"
PRODUCT_ID="12345" # Идентификатор товара, который нужно проверить
REQUESTS_COUNT=100 # Количество запросов для выполнения

for (( i=1; i<=REQUESTS_COUNT; i++ )); do
    echo "Запрос #$i ..."
    RESPONSE=$(curl -s "${API_ENDPOINT}?id=${PRODUCT_ID}")
    echo "Ответ API: $RESPONSE"
    if [[ "$RESPONSE" == "0" ]]; then
        echo "Обнаружен нулевой остаток на запросе #$i!"
    fi
    sleep 1 # Задержка между запросами в секундах
done
