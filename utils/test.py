from utils import parse_api_call
test_set = {
  "payments": [
    {
      "id": "FUFCWWyqixjTblfQfZcElmRh9AVZY",
      "created_at": "2024-05-11T19:14:53.432Z",
      "updated_at": "2024-05-11T19:14:54.413Z",
      "amount_money": {
        "amount": 3234,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:53.553Z",
          "captured_at": "2024-05-11T19:14:53.701Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "znemozICKbbLcwArXOzYqwUk0e4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:53.554Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:54.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3234,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3234,
        "currency": "USD"
      },
      "receipt_number": "FUFC",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/FUFCWWyqixjTblfQfZcElmRh9AVZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:53.432Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Jh1CVsJe1UksyIvDwyLJGqaVP32pqbOuOo9ftGus0vm6o"
    },
    {
      "id": "ZsC3tDItoN5v4gM7BYf2Q3af2VCZY",
      "created_at": "2024-05-11T19:14:52.637Z",
      "updated_at": "2024-05-11T19:14:53.945Z",
      "amount_money": {
        "amount": 3233,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:52.760Z",
          "captured_at": "2024-05-11T19:14:52.919Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "58zAE62kdSzqYYm4IIyP2KWw1e4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:52.761Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:53.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3233,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3233,
        "currency": "USD"
      },
      "receipt_number": "ZsC3",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/ZsC3tDItoN5v4gM7BYf2Q3af2VCZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:52.637Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "oVTM5EmplcJrWU2IFsKNOwmoOPxhx8LZEhTa0LvpNPN6o"
    },
    {
      "id": "Lv92jtlTmp78tpx8IoXFskhyY0GZY",
      "created_at": "2024-05-11T19:14:51.777Z",
      "updated_at": "2024-05-11T19:14:54.142Z",
      "amount_money": {
        "amount": 3232,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:51.898Z",
          "captured_at": "2024-05-11T19:14:52.048Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "dmxRaHnw0y96DGEEptksywdqJa4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:51.898Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:54.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3232,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3232,
        "currency": "USD"
      },
      "receipt_number": "Lv92",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/Lv92jtlTmp78tpx8IoXFskhyY0GZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:51.777Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "6vYUPHV5AbAaCjlsofJecaRG4Z5Y1fV6UKm68edAK5k6o"
    },
    {
      "id": "n1BE8NYilSF2VIoCfHqHrDB74YfZY",
      "created_at": "2024-05-11T19:14:50.714Z",
      "updated_at": "2024-05-11T19:14:51.374Z",
      "amount_money": {
        "amount": 3231,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:50.836Z",
          "captured_at": "2024-05-11T19:14:50.979Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "1cGvplUV9GT6wMwl1zc3OSKM2c4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:50.836Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:51.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3231,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3231,
        "currency": "USD"
      },
      "receipt_number": "n1BE",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/n1BE8NYilSF2VIoCfHqHrDB74YfZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:50.714Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "9JcsdrHMZooumHarHJ8XpXGfT4tqOAZYQaibpn2Bw1D6o"
    },
    {
      "id": "5GVqNWxOxtrfb1dFiFPa8Emh9tVZY",
      "created_at": "2024-05-11T19:14:49.850Z",
      "updated_at": "2024-05-11T19:14:51.333Z",
      "amount_money": {
        "amount": 3230,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:49.973Z",
          "captured_at": "2024-05-11T19:14:50.125Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "1oSESV4tgcW6dNAZ4lDT7Awema4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:49.973Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:51.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3230,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3230,
        "currency": "USD"
      },
      "receipt_number": "5GVq",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5GVqNWxOxtrfb1dFiFPa8Emh9tVZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:49.850Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Btxp9zRcanwUn6oYrw0wGreHcaG8My5myliBZa6EpFt6o"
    },
    {
      "id": "zp2H651JTRVaLJvG6ggvw6WtmaSZY",
      "created_at": "2024-05-11T19:14:49.029Z",
      "updated_at": "2024-05-11T19:14:50.334Z",
      "amount_money": {
        "amount": 3229,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:49.151Z",
          "captured_at": "2024-05-11T19:14:49.297Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "lYmw0yQ80sSO9ysVCCk4TfPTBb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:49.152Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:50.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3229,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3229,
        "currency": "USD"
      },
      "receipt_number": "zp2H",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/zp2H651JTRVaLJvG6ggvw6WtmaSZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:49.029Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "fBVcn7B1iWOf6CHWE82WgyqU2SPB9fLod4RPtIPnoML6o"
    },
    {
      "id": "hwcaCC7MWwFg2JPmlj0QvScUpJPZY",
      "created_at": "2024-05-11T19:14:48.245Z",
      "updated_at": "2024-05-11T19:14:49.292Z",
      "amount_money": {
        "amount": 3228,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:48.365Z",
          "captured_at": "2024-05-11T19:14:48.507Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "DHiQrjef6HEfyLZKPRlNNHKdYg4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:48.365Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:49.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3228,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3228,
        "currency": "USD"
      },
      "receipt_number": "hwca",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/hwcaCC7MWwFg2JPmlj0QvScUpJPZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:48.245Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "5axDx8qZLAF681968uxtI6KSbw0wQxFrLoCqgj7GsEh6o"
    },
    {
      "id": "Dtc5rWiEj5Y57dkvznbNoctFjKGZY",
      "created_at": "2024-05-11T19:14:47.407Z",
      "updated_at": "2024-05-11T19:14:49.018Z",
      "amount_money": {
        "amount": 3227,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:47.531Z",
          "captured_at": "2024-05-11T19:14:47.687Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "JGOZYnKmKNEV7CBi523R16rdjg4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:47.531Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:49.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3227,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3227,
        "currency": "USD"
      },
      "receipt_number": "Dtc5",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/Dtc5rWiEj5Y57dkvznbNoctFjKGZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:47.407Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "fK1LtMPs0TtatXTBV2ZhrYTjuMbMAiVTcV4NkyFsvxd6o"
    },
    {
      "id": "TfX4zx5Lxtq0XVQbiCVtYNWvSHgZY",
      "created_at": "2024-05-11T19:14:46.499Z",
      "updated_at": "2024-05-11T19:14:47.419Z",
      "amount_money": {
        "amount": 3226,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:46.621Z",
          "captured_at": "2024-05-11T19:14:46.762Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "7ZZ2Rw48HTFlTmLqm12eslqJcd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:46.621Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:47.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3226,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3226,
        "currency": "USD"
      },
      "receipt_number": "TfX4",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/TfX4zx5Lxtq0XVQbiCVtYNWvSHgZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:46.499Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "7MWoo6aSw2boqaiC0KpFMVTQmkOHiLa8gfwoO5HTioh6o"
    },
    {
      "id": "tg1ixCuABI4kbrYui986idlpBpJZY",
      "created_at": "2024-05-11T19:14:45.706Z",
      "updated_at": "2024-05-11T19:14:46.770Z",
      "amount_money": {
        "amount": 3225,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:45.824Z",
          "captured_at": "2024-05-11T19:14:45.976Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "90IZYdYghjnex0JHaRqFiL1SZc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:45.825Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:46.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 124,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3225,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3225,
        "currency": "USD"
      },
      "receipt_number": "tg1i",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tg1ixCuABI4kbrYui986idlpBpJZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:45.706Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "dB9bmST2b20zI4mj7EDkhCNLbMOaKAjAOnBvbw3wnn35o"
    },
    {
      "id": "f9v2f7WAVTrDAnLoAkpnKXytgW8YY",
      "created_at": "2024-05-11T19:14:44.917Z",
      "updated_at": "2024-05-11T19:14:47.101Z",
      "amount_money": {
        "amount": 3224,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:45.039Z",
          "captured_at": "2024-05-11T19:14:45.182Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "LXmNsA8x8tP4BgeVvTtZzx5pTh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:45.040Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:47.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3224,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3224,
        "currency": "USD"
      },
      "receipt_number": "f9v2",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/f9v2f7WAVTrDAnLoAkpnKXytgW8YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:44.917Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "qtAEw83t0UPxAvIDCMHZ53TmrJVgAmfSztUl81Z73Vb6o"
    },
    {
      "id": "H994i9qomOQ4af0IfGqYHh42TJ9YY",
      "created_at": "2024-05-11T19:14:44.134Z",
      "updated_at": "2024-05-11T19:14:46.056Z",
      "amount_money": {
        "amount": 3223,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:44.254Z",
          "captured_at": "2024-05-11T19:14:44.400Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "dkgbxwSmAXbqpMREx8HtIb43Nd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:44.254Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:46.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3223,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3223,
        "currency": "USD"
      },
      "receipt_number": "H994",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/H994i9qomOQ4af0IfGqYHh42TJ9YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:44.134Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Lu11WSoqqZMtuHNE1xM70YtiDG8XwZFLB6CRtbQXWxT6o"
    },
    {
      "id": "7bnSH0zJCJOwbIHzZvCtmH0JCPaZY",
      "created_at": "2024-05-11T19:14:43.331Z",
      "updated_at": "2024-05-11T19:14:44.182Z",
      "amount_money": {
        "amount": 3222,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:43.450Z",
          "captured_at": "2024-05-11T19:14:43.602Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "fPnodHK3UZjEfYqWr6eJn8px1Z4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:43.450Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:44.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3222,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3222,
        "currency": "USD"
      },
      "receipt_number": "7bnS",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/7bnSH0zJCJOwbIHzZvCtmH0JCPaZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:43.331Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "EmC239pPAqOyohxO8jBrRlHSoO60OCyc1WSkknkoV1r6o"
    },
    {
      "id": "1a0u8tuJXYVvwukk6fQNbaTyQB7YY",
      "created_at": "2024-05-11T19:14:42.530Z",
      "updated_at": "2024-05-11T19:14:43.982Z",
      "amount_money": {
        "amount": 3221,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:42.656Z",
          "captured_at": "2024-05-11T19:14:42.799Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "D1rdXWvWAntmnwTHQAxh5XbpyZ4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:42.656Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:43.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3221,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3221,
        "currency": "USD"
      },
      "receipt_number": "1a0u",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/1a0u8tuJXYVvwukk6fQNbaTyQB7YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:42.530Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "1K7wTUX4JCdGjADEL0jx3d0dougdFLT5Eye85q0wtSG6o"
    },
    {
      "id": "FugxwTbv1RB1I1VsAytdqPIVBMRZY",
      "created_at": "2024-05-11T19:14:41.718Z",
      "updated_at": "2024-05-11T19:14:42.778Z",
      "amount_money": {
        "amount": 3220,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:41.843Z",
          "captured_at": "2024-05-11T19:14:41.990Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "VCHsQ2eKLJtoRFUg5cdMIhIN7f4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:41.843Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:42.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3220,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3220,
        "currency": "USD"
      },
      "receipt_number": "Fugx",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/FugxwTbv1RB1I1VsAytdqPIVBMRZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:41.718Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "fPP2RD5OO0Jx2nhN68viSDYQSW4H1OFrul3MH3kjWbj6o"
    },
    {
      "id": "7L3gE0ofkwxc8DtNmkpAsviGazIZY",
      "created_at": "2024-05-11T19:14:40.833Z",
      "updated_at": "2024-05-11T19:14:43.148Z",
      "amount_money": {
        "amount": 3219,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:40.954Z",
          "captured_at": "2024-05-11T19:14:41.109Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "3nXvcu8bWWWjehAsoPbvghfqUf4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:40.954Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:43.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3219,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3219,
        "currency": "USD"
      },
      "receipt_number": "7L3g",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/7L3gE0ofkwxc8DtNmkpAsviGazIZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:40.833Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "4gisBr653WACxNeppQTkyIA41onjjuE6lyfsU5lJfZC6o"
    },
    {
      "id": "tQ5cJdaZ0Rn9MXt3wFrkGIyWpYeZY",
      "created_at": "2024-05-11T19:14:40.037Z",
      "updated_at": "2024-05-11T19:14:41.256Z",
      "amount_money": {
        "amount": 3218,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:40.159Z",
          "captured_at": "2024-05-11T19:14:40.310Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Rakq7Altgkai7L1gyGTQ0DbHGd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:40.159Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:41.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3218,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3218,
        "currency": "USD"
      },
      "receipt_number": "tQ5c",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tQ5cJdaZ0Rn9MXt3wFrkGIyWpYeZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:40.037Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "S0J3anHvCVx8Rz6SI4dm1VC0J3JWteftyMxcZRzM3TB6o"
    },
    {
      "id": "PXQEGvDSuvKK3Mz09qrDfOIdJDPZY",
      "created_at": "2024-05-11T19:14:39.252Z",
      "updated_at": "2024-05-11T19:14:41.082Z",
      "amount_money": {
        "amount": 3217,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:39.371Z",
          "captured_at": "2024-05-11T19:14:39.514Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "hEN2BNI03sC2yNmijD4x5HnFca4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:39.371Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:41.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3217,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3217,
        "currency": "USD"
      },
      "receipt_number": "PXQE",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/PXQEGvDSuvKK3Mz09qrDfOIdJDPZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:39.252Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "fiTVHZ28Ns5EVJTbCbBcj1PUf6LDA5uLWRIQuPpSvgh6o"
    },
    {
      "id": "7BmU5CHTstxSUMqI7M0RIpwuvxIZY",
      "created_at": "2024-05-11T19:14:38.463Z",
      "updated_at": "2024-05-11T19:14:40.040Z",
      "amount_money": {
        "amount": 3216,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:38.586Z",
          "captured_at": "2024-05-11T19:14:38.720Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "tAE6Mr9Q7cl8nxTVB2PCYuiqgc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:38.586Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:40.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3216,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3216,
        "currency": "USD"
      },
      "receipt_number": "7BmU",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/7BmU5CHTstxSUMqI7M0RIpwuvxIZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:38.463Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "bUmtbMF0WsAPR5OYQdS5Syb5cWvPgBCfnvgp1Cs6X8Q6o"
    },
    {
      "id": "dGIE1BLFbmrtdVQvsLuMvMseCYSZY",
      "created_at": "2024-05-11T19:14:37.663Z",
      "updated_at": "2024-05-11T19:14:38.164Z",
      "amount_money": {
        "amount": 3215,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:37.786Z",
          "captured_at": "2024-05-11T19:14:37.941Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "j9zFafXMHPWjPpGUGnwDw3F6Og4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:37.786Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:38.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3215,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3215,
        "currency": "USD"
      },
      "receipt_number": "dGIE",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/dGIE1BLFbmrtdVQvsLuMvMseCYSZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:37.663Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "xTCseVjviziHERE5OuUCblnZsBIzxcg01o3rY1a0mB55o"
    },
    {
      "id": "NYNuklTWZFHOIg0QsVE1sZjNX5DZY",
      "created_at": "2024-05-11T19:14:36.820Z",
      "updated_at": "2024-05-11T19:14:39.000Z",
      "amount_money": {
        "amount": 3214,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:36.952Z",
          "captured_at": "2024-05-11T19:14:37.107Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "JWu1Ev5oKZyDNr0ea6QbFvxaXb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:36.952Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:39.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3214,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3214,
        "currency": "USD"
      },
      "receipt_number": "NYNu",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/NYNuklTWZFHOIg0QsVE1sZjNX5DZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:36.820Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "y4nnzBcIeS7UPx3WyEn04HBwXeiHvDJq5FIHmlR60Bz6o"
    },
    {
      "id": "rV8IrV6HNDgPWwMbS0CUWWhCT4CZY",
      "created_at": "2024-05-11T19:14:36.023Z",
      "updated_at": "2024-05-11T19:14:38.053Z",
      "amount_money": {
        "amount": 3213,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:36.148Z",
          "captured_at": "2024-05-11T19:14:36.302Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "3fdEYIqQoKGf2ptHda2C8JlW3f4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:36.148Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:38.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3213,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3213,
        "currency": "USD"
      },
      "receipt_number": "rV8I",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/rV8IrV6HNDgPWwMbS0CUWWhCT4CZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:36.023Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "UyGsIWDyCruQbGqARxE5s5eClc22GqvF0AbhScANwFi6o"
    },
    {
      "id": "poC2bBPPQ1iDS9iU2oHYm263DgGZY",
      "created_at": "2024-05-11T19:14:35.196Z",
      "updated_at": "2024-05-11T19:14:36.815Z",
      "amount_money": {
        "amount": 3212,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:35.317Z",
          "captured_at": "2024-05-11T19:14:35.468Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "HdiJMoSLtTdnf7C6FgAMIT418h4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:35.317Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:36.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3212,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3212,
        "currency": "USD"
      },
      "receipt_number": "poC2",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/poC2bBPPQ1iDS9iU2oHYm263DgGZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:35.196Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "JUgK6Ah3o8onGxVcfHlOMioEER58fKxWT2nfZvCQRMh6o"
    },
    {
      "id": "rdeH7tUTQKWozLqrXJ7SpFOZQCBZY",
      "created_at": "2024-05-11T19:14:34.414Z",
      "updated_at": "2024-05-11T19:14:35.772Z",
      "amount_money": {
        "amount": 3211,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:34.538Z",
          "captured_at": "2024-05-11T19:14:34.686Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "RSy1wGNC5mluZ81WktV9fxna8c4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:34.538Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:35.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3211,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3211,
        "currency": "USD"
      },
      "receipt_number": "rdeH",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/rdeH7tUTQKWozLqrXJ7SpFOZQCBZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:34.414Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Mev0aalmuN5BAJsyJDPDlkvXWOnAOuEnaeuQd7EOyE65o"
    },
    {
      "id": "v7MFS1AqHLrAjKP5ytcQsNN873EZY",
      "created_at": "2024-05-11T19:14:33.619Z",
      "updated_at": "2024-05-11T19:14:34.908Z",
      "amount_money": {
        "amount": 3210,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:33.742Z",
          "captured_at": "2024-05-11T19:14:33.887Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "xeeOVimKdsTxQehvZDuwtd1Dcg4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:33.742Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:34.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3210,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3210,
        "currency": "USD"
      },
      "receipt_number": "v7MF",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/v7MFS1AqHLrAjKP5ytcQsNN873EZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:33.619Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "698YwXQJ92wUtBFLJu9r0TGu5M1h4h3rkDnJf7YpIKP6o"
    },
    {
      "id": "dEzcOby0yW1cdmECR3LKmPTRgNQZY",
      "created_at": "2024-05-11T19:14:32.824Z",
      "updated_at": "2024-05-11T19:14:35.072Z",
      "amount_money": {
        "amount": 3209,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:32.946Z",
          "captured_at": "2024-05-11T19:14:33.098Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "FgO4rZJ4K768T7whIDTSorr8nh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:32.946Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:35.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3209,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3209,
        "currency": "USD"
      },
      "receipt_number": "dEzc",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/dEzcOby0yW1cdmECR3LKmPTRgNQZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:32.824Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "7FP2zcYekOSDdHj2DT9wNPTGtUOxz2955Ot1ZBDmZbz6o"
    },
    {
      "id": "LR8PkTqgmN0CwADEr1Sq2gs7zAcZY",
      "created_at": "2024-05-11T19:14:31.992Z",
      "updated_at": "2024-05-11T19:14:33.642Z",
      "amount_money": {
        "amount": 3208,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:32.114Z",
          "captured_at": "2024-05-11T19:14:32.267Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "njbmtTPOSIfo5yVzPs9NRJ3Cgd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:32.114Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:33.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3208,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3208,
        "currency": "USD"
      },
      "receipt_number": "LR8P",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/LR8PkTqgmN0CwADEr1Sq2gs7zAcZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:31.992Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "mIpqCRHitdwxnHRuEAd8wgHqf93DEo4ACh5ZgWoEmkc6o"
    },
    {
      "id": "PrqmNQFcOXRTmJ0XHGe3d3FNeORZY",
      "created_at": "2024-05-11T19:14:31.183Z",
      "updated_at": "2024-05-11T19:14:32.759Z",
      "amount_money": {
        "amount": 3207,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:31.305Z",
          "captured_at": "2024-05-11T19:14:31.450Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "f5Y4oQIwprfXeIvTybBaYPA8Qf4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:31.305Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:32.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3207,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3207,
        "currency": "USD"
      },
      "receipt_number": "Prqm",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/PrqmNQFcOXRTmJ0XHGe3d3FNeORZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:31.183Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "t5yHUYmU5WHc0JC199mp4bFSClCb6eHO9nhgZz1dHQW6o"
    },
    {
      "id": "Pf6XAaEpc0cmref7fPQOYB3o4U8YY",
      "created_at": "2024-05-11T19:14:30.391Z",
      "updated_at": "2024-05-11T19:14:31.718Z",
      "amount_money": {
        "amount": 3206,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:30.515Z",
          "captured_at": "2024-05-11T19:14:30.666Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "hYlHs0uWJfcEfBA8TNSeSQW0Wi4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:30.515Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:31.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3206,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3206,
        "currency": "USD"
      },
      "receipt_number": "Pf6X",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/Pf6XAaEpc0cmref7fPQOYB3o4U8YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:30.391Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "vaCyqL6YMoYWHZhHFR79dAdF0Jwtjf17tEBKlHnfdiq6o"
    },
    {
      "id": "PxNOLx7wM9yfsXLpTEHVscs1JMEZY",
      "created_at": "2024-05-11T19:14:29.579Z",
      "updated_at": "2024-05-11T19:14:30.580Z",
      "amount_money": {
        "amount": 3205,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:29.702Z",
          "captured_at": "2024-05-11T19:14:29.855Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "35YvaAwDgooabIL8HYwc7ksere4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:29.702Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:30.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3205,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3205,
        "currency": "USD"
      },
      "receipt_number": "PxNO",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/PxNOLx7wM9yfsXLpTEHVscs1JMEZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:29.579Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "LHCflKHdqHexmACURkhBNZdZMijo9NlqdGUjwwE3P8d6o"
    },
    {
      "id": "NuKxTSFgDjIfVY5Q8gTLSCwYtdJZY",
      "created_at": "2024-05-11T19:14:28.756Z",
      "updated_at": "2024-05-11T19:14:30.814Z",
      "amount_money": {
        "amount": 3204,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:28.877Z",
          "captured_at": "2024-05-11T19:14:29.025Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "9aDNG0qhqhABmPKiVaZLLLfBYe4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:28.877Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:30.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3204,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3204,
        "currency": "USD"
      },
      "receipt_number": "NuKx",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/NuKxTSFgDjIfVY5Q8gTLSCwYtdJZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:28.756Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "HqlhJNQWQE4EhxjYu801lT91EWIuO8ei6AKv7DLYGIL6o"
    },
    {
      "id": "lCQ8ix0a12r8EOFY3tnr6jsY097YY",
      "created_at": "2024-05-11T19:14:27.914Z",
      "updated_at": "2024-05-11T19:14:29.813Z",
      "amount_money": {
        "amount": 3203,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:28.034Z",
          "captured_at": "2024-05-11T19:14:28.182Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "DxJtllz68Ch62CPdzsyaKe9the4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:28.034Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:29.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3203,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3203,
        "currency": "USD"
      },
      "receipt_number": "lCQ8",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/lCQ8ix0a12r8EOFY3tnr6jsY097YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:27.914Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "IyeUrok6oTxA8MzTK4dT681vBHOiop561pFpIIlbmrd6o"
    },
    {
      "id": "ty0dFg0lInuRSwZzB9Uh62WFjWfZY",
      "created_at": "2024-05-11T19:14:27.107Z",
      "updated_at": "2024-05-11T19:14:28.778Z",
      "amount_money": {
        "amount": 3202,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:27.231Z",
          "captured_at": "2024-05-11T19:14:27.380Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "HzvctuJBm04uiprAblcCoNAlsZ4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:27.231Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:28.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3202,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3202,
        "currency": "USD"
      },
      "receipt_number": "ty0d",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/ty0dFg0lInuRSwZzB9Uh62WFjWfZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:27.107Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "lvwIJrySJFzrn5TnqQQ7OPDLDrjLztAzjmKOLtXcFXq6o"
    },
    {
      "id": "THj8JeXSvxg6Uw4yQqv0nVQhc9RZY",
      "created_at": "2024-05-11T19:14:26.283Z",
      "updated_at": "2024-05-11T19:14:27.739Z",
      "amount_money": {
        "amount": 3201,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:26.408Z",
          "captured_at": "2024-05-11T19:14:26.569Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Lx12mLyZlYvHwuQjXKPBq7yymb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:26.408Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:27.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3201,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3201,
        "currency": "USD"
      },
      "receipt_number": "THj8",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/THj8JeXSvxg6Uw4yQqv0nVQhc9RZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:26.283Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "K5KqbaoVhtYgntmW6bqJFId1XdJMO851QoAAyXRnZgh6o"
    },
    {
      "id": "1s75yz1eppaR84lOcIQjHuO52gJZY",
      "created_at": "2024-05-11T19:14:25.501Z",
      "updated_at": "2024-05-11T19:14:26.621Z",
      "amount_money": {
        "amount": 3200,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:25.620Z",
          "captured_at": "2024-05-11T19:14:25.773Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "TZL8gJNNni5f6CuSiPSTPpgxda4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:25.620Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:26.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3200,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3200,
        "currency": "USD"
      },
      "receipt_number": "1s75",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/1s75yz1eppaR84lOcIQjHuO52gJZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:25.501Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "6GSnR0nDcdc2HUxTu43qwxOT8xBzYeWT73o96TYi5ag6o"
    },
    {
      "id": "Hzy1iLzWpA6Id7Gy35sziOPazGKZY",
      "created_at": "2024-05-11T19:14:24.710Z",
      "updated_at": "2024-05-11T19:14:25.831Z",
      "amount_money": {
        "amount": 3199,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:24.833Z",
          "captured_at": "2024-05-11T19:14:24.980Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "TbYeqnLrPWDsCti4yne6BWkoia4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:24.834Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:25.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3199,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3199,
        "currency": "USD"
      },
      "receipt_number": "Hzy1",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/Hzy1iLzWpA6Id7Gy35sziOPazGKZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:24.710Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "pMd1PUYeeKnxaGvZIaPYOcKMKfFcFDgB2qjJINk5AtN6o"
    },
    {
      "id": "nrqLOyAPhrM4eQ2L9BpPSGSlYq5YY",
      "created_at": "2024-05-11T19:14:23.926Z",
      "updated_at": "2024-05-11T19:14:25.495Z",
      "amount_money": {
        "amount": 3198,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:24.049Z",
          "captured_at": "2024-05-11T19:14:24.189Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "nNUUXNjXCYC0pu9fExYJLhknph4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:24.050Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:25.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3198,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3198,
        "currency": "USD"
      },
      "receipt_number": "nrqL",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/nrqLOyAPhrM4eQ2L9BpPSGSlYq5YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:23.926Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "iSH5S6es1FBEPWpLGFRotqn50GPh0o4Na3JHwUgqXfm6o"
    },
    {
      "id": "9CADU3YWRKeXreeQj1F4CKZ2CEFZY",
      "created_at": "2024-05-11T19:14:23.140Z",
      "updated_at": "2024-05-11T19:14:24.787Z",
      "amount_money": {
        "amount": 3197,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:23.263Z",
          "captured_at": "2024-05-11T19:14:23.409Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "5wnZyI3TuXCmTLHplhsbVBc3Ji4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:23.263Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:24.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3197,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3197,
        "currency": "USD"
      },
      "receipt_number": "9CAD",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/9CADU3YWRKeXreeQj1F4CKZ2CEFZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:23.140Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "90RI8VhMmgKgPfYQS8TGIRrrWwu7qabavdSuFdk9BKp6o"
    },
    {
      "id": "5qvUiZ0zInqVFV3tabxDX0FAWj7YY",
      "created_at": "2024-05-11T19:14:22.366Z",
      "updated_at": "2024-05-11T19:14:23.449Z",
      "amount_money": {
        "amount": 3196,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:22.487Z",
          "captured_at": "2024-05-11T19:14:22.636Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "5g5W6Yv5NGx3FjEiGhtx3uo5na4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:22.488Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:23.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3196,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3196,
        "currency": "USD"
      },
      "receipt_number": "5qvU",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5qvUiZ0zInqVFV3tabxDX0FAWj7YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:22.366Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "ti2IYrRgcNbUep1dOPvwf0tUKaPUAWazb87PTn310db6o"
    },
    {
      "id": "lGIZtwZWaFHXytEoAgoPxTPPp1LZY",
      "created_at": "2024-05-11T19:14:21.538Z",
      "updated_at": "2024-05-11T19:14:22.472Z",
      "amount_money": {
        "amount": 3195,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:21.661Z",
          "captured_at": "2024-05-11T19:14:21.811Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "xoFD9N8eG8h2Kyiuii3pNSTqyZ4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:21.661Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:22.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3195,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3195,
        "currency": "USD"
      },
      "receipt_number": "lGIZ",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/lGIZtwZWaFHXytEoAgoPxTPPp1LZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:21.538Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "KgntuEI8pv04LXsYwZM8U73kcG6FSHoA2ZIjHD0zBGe6o"
    },
    {
      "id": "nfO0yrEoDBl9MoxSNvUiTzZZeTWZY",
      "created_at": "2024-05-11T19:14:20.736Z",
      "updated_at": "2024-05-11T19:14:22.717Z",
      "amount_money": {
        "amount": 3194,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:20.860Z",
          "captured_at": "2024-05-11T19:14:21.006Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "PtM9vXL4lXspWmInBPqUPPIB7c4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:20.860Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:22.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3194,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3194,
        "currency": "USD"
      },
      "receipt_number": "nfO0",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/nfO0yrEoDBl9MoxSNvUiTzZZeTWZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:20.736Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "ngTIXvSfJUsy4uNiTJccjGMOBTNaMvuKv3isjQuxG1A6o"
    },
    {
      "id": "5GTLiGIWah0acV4BC6E1Y8vr2FRZY",
      "created_at": "2024-05-11T19:14:19.948Z",
      "updated_at": "2024-05-11T19:14:21.365Z",
      "amount_money": {
        "amount": 3193,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:20.073Z",
          "captured_at": "2024-05-11T19:14:20.218Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "zNzz6fx7TgIraZbp9C1KOQx8wZ4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:20.073Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:21.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3193,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3193,
        "currency": "USD"
      },
      "receipt_number": "5GTL",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5GTLiGIWah0acV4BC6E1Y8vr2FRZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:19.948Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Um0jHvxjuzrrowzuei4mZtRtnPGlOIZVl8TOZ9JgnfN6o"
    },
    {
      "id": "RqBkYHfhOvQmhJEVD0NCI3jb1cMZY",
      "created_at": "2024-05-11T19:14:19.150Z",
      "updated_at": "2024-05-11T19:14:20.586Z",
      "amount_money": {
        "amount": 3192,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:19.270Z",
          "captured_at": "2024-05-11T19:14:19.420Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "brKYWgVRClR0FDjtV27MWh1aPi4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:19.270Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:20.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3192,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3192,
        "currency": "USD"
      },
      "receipt_number": "RqBk",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/RqBkYHfhOvQmhJEVD0NCI3jb1cMZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:19.150Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Y83wjCPlhiXAvgVEnNnRd3EOl7Kn9lLLB7ij8w7ctmW6o"
    },
    {
      "id": "znlfEYszyfDbsCteYo0mCIX6NyQZY",
      "created_at": "2024-05-11T19:14:18.342Z",
      "updated_at": "2024-05-11T19:14:19.538Z",
      "amount_money": {
        "amount": 3191,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:18.462Z",
          "captured_at": "2024-05-11T19:14:18.617Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "x6ybaMxnsKQM0HiHKOUmEWoLEh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:18.463Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:19.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3191,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3191,
        "currency": "USD"
      },
      "receipt_number": "znlf",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/znlfEYszyfDbsCteYo0mCIX6NyQZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:18.342Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "9ADcRDRlnwomZnDOlygnktPpbA3xpkOJQ3YFmOEKObr6o"
    },
    {
      "id": "V2cF9gHuxqMf35RtjKEd2fcw96TZY",
      "created_at": "2024-05-11T19:14:17.542Z",
      "updated_at": "2024-05-11T19:14:18.362Z",
      "amount_money": {
        "amount": 3190,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:17.665Z",
          "captured_at": "2024-05-11T19:14:17.817Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Jk5xBbPdeif8FsfrPABb5Gkdna4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:17.665Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:18.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 123,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3190,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3190,
        "currency": "USD"
      },
      "receipt_number": "V2cF",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/V2cF9gHuxqMf35RtjKEd2fcw96TZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:17.542Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Imi7HURV3oLHjEivVMmEy4GvBhnnWSQHICawkWjzuBG6o"
    },
    {
      "id": "tuQ6827fcoUAYGjQT0ihFWNxJhIZY",
      "created_at": "2024-05-11T19:14:16.760Z",
      "updated_at": "2024-05-11T19:14:18.493Z",
      "amount_money": {
        "amount": 3189,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:16.882Z",
          "captured_at": "2024-05-11T19:14:17.031Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "f1MbIspjZqrt0GLNL2sDb4EAog4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:16.882Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:18.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3189,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3189,
        "currency": "USD"
      },
      "receipt_number": "tuQ6",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tuQ6827fcoUAYGjQT0ihFWNxJhIZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:16.760Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "1Zs90s72jkaBsmX0rLMf8N0YsR2o3bVGtJJLNeZUDwX6o"
    },
    {
      "id": "hAGHqLdBFcmKSIXgha4oKIPZjuPZY",
      "created_at": "2024-05-11T19:14:15.974Z",
      "updated_at": "2024-05-11T19:14:17.344Z",
      "amount_money": {
        "amount": 3188,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:16.095Z",
          "captured_at": "2024-05-11T19:14:16.248Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "jLYo4pPYimvm892BMFFAKSZOxh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:16.095Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:17.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3188,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3188,
        "currency": "USD"
      },
      "receipt_number": "hAGH",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/hAGHqLdBFcmKSIXgha4oKIPZjuPZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:15.974Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "45Iw93b05sYEQYc8q465yeRQIwOpl8xUUNnY0PEL1TU6o"
    },
    {
      "id": "tUdNhpKfbZrRuhkk0iHPvi1yZsCZY",
      "created_at": "2024-05-11T19:14:15.163Z",
      "updated_at": "2024-05-11T19:14:16.457Z",
      "amount_money": {
        "amount": 3187,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:15.285Z",
          "captured_at": "2024-05-11T19:14:15.431Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "b3yjHUUINBMDOVghfMUypj5O9a4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:15.285Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:16.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3187,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3187,
        "currency": "USD"
      },
      "receipt_number": "tUdN",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tUdNhpKfbZrRuhkk0iHPvi1yZsCZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:15.163Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "NH3bV5sJOCmmbRI6VmNibakSNY1BnYmkNqiy2yh5V8S6o"
    },
    {
      "id": "7H5I9VD1HSyLrXkTKo4WX7gWw8ZZY",
      "created_at": "2024-05-11T19:14:14.379Z",
      "updated_at": "2024-05-11T19:14:15.279Z",
      "amount_money": {
        "amount": 3186,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:14.509Z",
          "captured_at": "2024-05-11T19:14:14.651Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "hSU2tfQs8ME97Kk2vzK21hLnHd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:14.509Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:15.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3186,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3186,
        "currency": "USD"
      },
      "receipt_number": "7H5I",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/7H5I9VD1HSyLrXkTKo4WX7gWw8ZZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:14.379Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "TcSDePShc4uOUHsZ7nldxd6Eo1QV3V2aifZ1FH1vdD16o"
    },
    {
      "id": "R8KoqXFVCCRRda7SOYm0vWdqUKMZY",
      "created_at": "2024-05-11T19:14:13.591Z",
      "updated_at": "2024-05-11T19:14:14.294Z",
      "amount_money": {
        "amount": 3185,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:13.717Z",
          "captured_at": "2024-05-11T19:14:13.863Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "TZJ7uEZqKeGFAPKLGvENS4XRWh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:13.717Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:14.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3185,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3185,
        "currency": "USD"
      },
      "receipt_number": "R8Ko",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/R8KoqXFVCCRRda7SOYm0vWdqUKMZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:13.591Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "cJqNqQu6uA40V1fF74SYgQT2Mz7Gof9OQvP5551h46x6o"
    },
    {
      "id": "vpfPAlgTMtSXICM4t6k11WvectWZY",
      "created_at": "2024-05-11T19:14:12.773Z",
      "updated_at": "2024-05-11T19:14:14.271Z",
      "amount_money": {
        "amount": 3184,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:12.895Z",
          "captured_at": "2024-05-11T19:14:13.052Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "108oLNaw8gAIE8XlWaX9tCKlha4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:12.895Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:14.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3184,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3184,
        "currency": "USD"
      },
      "receipt_number": "vpfP",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/vpfPAlgTMtSXICM4t6k11WvectWZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:12.773Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "2kCKqkF9lUewNIl4D9C1aEzwhH9WK6t7BWZ7BJGaI2r6o"
    },
    {
      "id": "j31r735YehsYSHTs3l5Cybzi0CCZY",
      "created_at": "2024-05-11T19:14:11.664Z",
      "updated_at": "2024-05-11T19:14:12.367Z",
      "amount_money": {
        "amount": 3183,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:11.789Z",
          "captured_at": "2024-05-11T19:14:11.937Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Hla32S9AnchUIOGYkXU10m04kb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:11.789Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:12.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3183,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3183,
        "currency": "USD"
      },
      "receipt_number": "j31r",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/j31r735YehsYSHTs3l5Cybzi0CCZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:11.664Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "H61LvFyBz3LjLVHW160mblPUMoFSzGiJ02Cd82jDgV45o"
    },
    {
      "id": "zN66nXIsshawZR157WtVCx96K75YY",
      "created_at": "2024-05-11T19:14:10.830Z",
      "updated_at": "2024-05-11T19:14:12.376Z",
      "amount_money": {
        "amount": 3182,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:10.953Z",
          "captured_at": "2024-05-11T19:14:11.097Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "jDwqAI9ZCwf2glMZBElkjfPIPf4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:10.953Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:12.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3182,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3182,
        "currency": "USD"
      },
      "receipt_number": "zN66",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/zN66nXIsshawZR157WtVCx96K75YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:10.830Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "io5U6gg4IjeYdOsZP25XaUAHtarHU8B5KwvgL5RNoAH6o"
    },
    {
      "id": "ZAQrYSlVCGzEKpuuA7SyitZg4dRZY",
      "created_at": "2024-05-11T19:14:09.978Z",
      "updated_at": "2024-05-11T19:14:11.195Z",
      "amount_money": {
        "amount": 3181,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:10.107Z",
          "captured_at": "2024-05-11T19:14:10.263Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "9UykVGl3Hj08lUmavTOFFFgMIe4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:10.107Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:11.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3181,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3181,
        "currency": "USD"
      },
      "receipt_number": "ZAQr",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/ZAQrYSlVCGzEKpuuA7SyitZg4dRZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:09.978Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "K4m9COGpwxHMiIcy4gVK8tutkfDPLJhsjKQOef273Um6o"
    },
    {
      "id": "5q57rFiuneTmuSiDsqXqX0TW0TTZY",
      "created_at": "2024-05-11T19:14:09.191Z",
      "updated_at": "2024-05-11T19:14:10.526Z",
      "amount_money": {
        "amount": 3180,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:09.315Z",
          "captured_at": "2024-05-11T19:14:09.456Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "vTvlTQ6WNhb9BJzXYVdodbVSfb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:09.315Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:10.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3180,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3180,
        "currency": "USD"
      },
      "receipt_number": "5q57",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5q57rFiuneTmuSiDsqXqX0TW0TTZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:09.191Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "W8PUsFmtjMo2p9MBg6ZZ4jvDAHJhBeAr5Npg8ETbLHe6o"
    },
    {
      "id": "BAESoeHQWCH5YcmrE4g9eSj8ShRZY",
      "created_at": "2024-05-11T19:14:08.396Z",
      "updated_at": "2024-05-11T19:14:09.305Z",
      "amount_money": {
        "amount": 3179,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:08.517Z",
          "captured_at": "2024-05-11T19:14:08.671Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "7lveHxDg9PBGFRHmjWldonDtub4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:08.517Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:09.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3179,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3179,
        "currency": "USD"
      },
      "receipt_number": "BAES",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/BAESoeHQWCH5YcmrE4g9eSj8ShRZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:08.396Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "IK3WlVK5FCXGaKz3DlyYb9ojh3M7wMp9efgwjX0mHJC6o"
    },
    {
      "id": "teA2ECLdmZUQTRBIHAymIZW5D8LZY",
      "created_at": "2024-05-11T19:14:07.548Z",
      "updated_at": "2024-05-11T19:14:08.262Z",
      "amount_money": {
        "amount": 3178,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:07.673Z",
          "captured_at": "2024-05-11T19:14:07.828Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "R2ITusk0O5qayBjaY2kocWaDWe4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:07.673Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:08.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3178,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3178,
        "currency": "USD"
      },
      "receipt_number": "teA2",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/teA2ECLdmZUQTRBIHAymIZW5D8LZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:07.548Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "tmG8NGsGTLFhy2aCheiIFsBdwWBloO1QqmY6M8urdjV6o"
    },
    {
      "id": "VczlsmG0syACjA7be863Ib2EEd9YY",
      "created_at": "2024-05-11T19:14:06.694Z",
      "updated_at": "2024-05-11T19:14:07.220Z",
      "amount_money": {
        "amount": 3177,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:06.817Z",
          "captured_at": "2024-05-11T19:14:06.974Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "b3YwiNZMzHOJkl25xHmz58yJBc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:06.818Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:07.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3177,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3177,
        "currency": "USD"
      },
      "receipt_number": "Vczl",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/VczlsmG0syACjA7be863Ib2EEd9YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:06.694Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "n510WsAFJMQNOTn8W7nimQ4T5P6SabsaRS9YazubaMQ6o"
    },
    {
      "id": "zjr7IGH4FwwX6VD3HxOY3til4vFZY",
      "created_at": "2024-05-11T19:14:05.897Z",
      "updated_at": "2024-05-11T19:14:07.160Z",
      "amount_money": {
        "amount": 3176,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:06.018Z",
          "captured_at": "2024-05-11T19:14:06.163Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "dYqd4j7rzkPc9UZpZ39IbQ0bCd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:06.018Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:07.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3176,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3176,
        "currency": "USD"
      },
      "receipt_number": "zjr7",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/zjr7IGH4FwwX6VD3HxOY3til4vFZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:05.897Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "5jPc4CygLuhu7fscKOsigciAnzzweWaF57pNid6PqSt6o"
    },
    {
      "id": "rjldBHyAOwe3nPabCW1x6e59ytRZY",
      "created_at": "2024-05-11T19:14:05.072Z",
      "updated_at": "2024-05-11T19:14:07.109Z",
      "amount_money": {
        "amount": 3175,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:05.204Z",
          "captured_at": "2024-05-11T19:14:05.364Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "xmi8qpCMYuVfRXlWh38liZPnUd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:05.204Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:07.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3175,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3175,
        "currency": "USD"
      },
      "receipt_number": "rjld",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/rjldBHyAOwe3nPabCW1x6e59ytRZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:05.072Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "X8UmaiV0U4A5sGYpin9fFwrqyt7SHPqAUxIm1awCFeK6o"
    },
    {
      "id": "dQPvqvGq2yi7sKcTg5lbqpbCWVAZY",
      "created_at": "2024-05-11T19:14:04.284Z",
      "updated_at": "2024-05-11T19:14:05.165Z",
      "amount_money": {
        "amount": 3174,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:04.407Z",
          "captured_at": "2024-05-11T19:14:04.553Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "XvRYV0V4SDndNq5Q6FspTtvQlb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:04.407Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:05.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3174,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3174,
        "currency": "USD"
      },
      "receipt_number": "dQPv",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/dQPvqvGq2yi7sKcTg5lbqpbCWVAZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:04.284Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "G2AGLTBlf6L8bNMsqwwussQb9RKGuV4TJx7JlrF7jvi6o"
    },
    {
      "id": "JokNIZLUjXZ7tmhmALfZ2pxzt5DZY",
      "created_at": "2024-05-11T19:14:03.493Z",
      "updated_at": "2024-05-11T19:14:04.447Z",
      "amount_money": {
        "amount": 3173,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:03.614Z",
          "captured_at": "2024-05-11T19:14:03.765Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "1s6Bp0V4AEPlUj9UUsSVbY6pTe4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:03.614Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:04.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3173,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3173,
        "currency": "USD"
      },
      "receipt_number": "JokN",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/JokNIZLUjXZ7tmhmALfZ2pxzt5DZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:03.493Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "PQ2qXgAezuXt8nhLtwSo3X2JSvD07A3NTuXApam1mtG6o"
    },
    {
      "id": "tWSL9Mf1sKzJPn5ElZFPW8Gf4WVZY",
      "created_at": "2024-05-11T19:14:02.643Z",
      "updated_at": "2024-05-11T19:14:04.100Z",
      "amount_money": {
        "amount": 3172,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:02.764Z",
          "captured_at": "2024-05-11T19:14:02.921Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "pqkFXtCa1cCfCoXDedDESPjSvh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:02.764Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:04.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3172,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3172,
        "currency": "USD"
      },
      "receipt_number": "tWSL",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tWSL9Mf1sKzJPn5ElZFPW8Gf4WVZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:02.643Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "2T3TUaRY5Pqg1PdHKCQ6jsCoaY4DFgIeXgH17nBilZp6o"
    },
    {
      "id": "DJMUyJduGrMQUWAznEDy9yJZH5HZY",
      "created_at": "2024-05-11T19:14:01.851Z",
      "updated_at": "2024-05-11T19:14:03.183Z",
      "amount_money": {
        "amount": 3171,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:01.974Z",
          "captured_at": "2024-05-11T19:14:02.118Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "dMsNIKs7Twm2MikUUbaLlDkJzh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:01.974Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:03.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3171,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3171,
        "currency": "USD"
      },
      "receipt_number": "DJMU",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/DJMUyJduGrMQUWAznEDy9yJZH5HZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:01.851Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "64DPYPVZEUCtPlYFSyNhDXkNJVc8YR1lFXJ4Pq5SfpR6o"
    },
    {
      "id": "DRcSCnJXWrdVwnmSAEGlvUpVQaIZY",
      "created_at": "2024-05-11T19:14:01.040Z",
      "updated_at": "2024-05-11T19:14:03.066Z",
      "amount_money": {
        "amount": 3170,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:01.162Z",
          "captured_at": "2024-05-11T19:14:01.319Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "bdlJSoqGdsW2bPwrXVPlFUfi2b4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:01.162Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:03.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3170,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3170,
        "currency": "USD"
      },
      "receipt_number": "DRcS",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/DRcSCnJXWrdVwnmSAEGlvUpVQaIZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:01.040Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "lIGDApvsdVcEtkUn2cIhH4dv9hXSM4XIOEGKApXUamA6o"
    },
    {
      "id": "rlu19yThfTXbhG8ObCHYcY4WsxLZY",
      "created_at": "2024-05-11T19:14:00.254Z",
      "updated_at": "2024-05-11T19:14:02.143Z",
      "amount_money": {
        "amount": 3169,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:14:00.374Z",
          "captured_at": "2024-05-11T19:14:00.524Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "PbTnw58h8WYdWoKaXNvUPFC1uh4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:14:00.374Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:02.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3169,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3169,
        "currency": "USD"
      },
      "receipt_number": "rlu1",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/rlu19yThfTXbhG8ObCHYcY4WsxLZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:14:00.254Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "rC6PKwHeVObWtfhAeZqMkNqHr5vqGlr0cF3drhOBPOW6o"
    },
    {
      "id": "NaqO5RM6amSjYh8EkpVSTi59OUeZY",
      "created_at": "2024-05-11T19:13:59.470Z",
      "updated_at": "2024-05-11T19:14:01.019Z",
      "amount_money": {
        "amount": 3168,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:59.591Z",
          "captured_at": "2024-05-11T19:13:59.737Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "BGAlyBZ1E2LpSvnpwjoFYVdf6g4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:59.591Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:14:01.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3168,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3168,
        "currency": "USD"
      },
      "receipt_number": "NaqO",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/NaqO5RM6amSjYh8EkpVSTi59OUeZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:59.470Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "KeHOLrFeCIg3tiliOYeeXTQ216nj9BHpl9UfzvQlm6q6o"
    },
    {
      "id": "tQZIvBYQ6rJent2WP4hxHSmVxgaZY",
      "created_at": "2024-05-11T19:13:58.620Z",
      "updated_at": "2024-05-11T19:13:59.333Z",
      "amount_money": {
        "amount": 3167,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:58.748Z",
          "captured_at": "2024-05-11T19:13:58.903Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "ZuyvgYiwHh7laIhIgNc8YNmA6Z4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:58.748Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:59.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3167,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3167,
        "currency": "USD"
      },
      "receipt_number": "tQZI",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tQZIvBYQ6rJent2WP4hxHSmVxgaZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:58.620Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "qYA5rmJlrbwKLSAmnC6uFCfgAu5zIbmtUT5vmrEdMrg6o"
    },
    {
      "id": "5wmEbO5NI1GbeqsWZ04q3xsUaVUZY",
      "created_at": "2024-05-11T19:13:57.786Z",
      "updated_at": "2024-05-11T19:13:59.967Z",
      "amount_money": {
        "amount": 3166,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:57.911Z",
          "captured_at": "2024-05-11T19:13:58.075Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "FoklJpgpvEuSxHSownoewXNcfc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:57.912Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:59.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3166,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3166,
        "currency": "USD"
      },
      "receipt_number": "5wmE",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5wmEbO5NI1GbeqsWZ04q3xsUaVUZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:57.786Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "jwCE2BlNRxwoEgssIE7alqkyBbeRFqCm5qHD3WsGyAi6o"
    },
    {
      "id": "7l464eS335Z2naGX7umvFpQBeQBZY",
      "created_at": "2024-05-11T19:13:57.000Z",
      "updated_at": "2024-05-11T19:13:58.962Z",
      "amount_money": {
        "amount": 3165,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:57.125Z",
          "captured_at": "2024-05-11T19:13:57.268Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "5U9DqAoHnIriGXkgvSOzgACwcg4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:57.125Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:58.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3165,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3165,
        "currency": "USD"
      },
      "receipt_number": "7l46",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/7l464eS335Z2naGX7umvFpQBeQBZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:57.000Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "goHkpF2wed2lX3lEMuamYrLTWSbmWX583shS21NPx9p6o"
    },
    {
      "id": "XBbIGNL2oyhzF5QwsKmZVtaL268YY",
      "created_at": "2024-05-11T19:13:56.198Z",
      "updated_at": "2024-05-11T19:13:57.271Z",
      "amount_money": {
        "amount": 3164,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:56.321Z",
          "captured_at": "2024-05-11T19:13:56.474Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "R228lD2rclnJVpbgBM6oYeu7Gg4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:56.321Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:57.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3164,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3164,
        "currency": "USD"
      },
      "receipt_number": "XBbI",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/XBbIGNL2oyhzF5QwsKmZVtaL268YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:56.198Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Iq30B9XqW3OYYRSWkx6ZFanEX8HigTZuJ7mILDHBPda6o"
    },
    {
      "id": "RqZkMaK98ZkH7wFiMcEQ7UYGkhWZY",
      "created_at": "2024-05-11T19:13:55.412Z",
      "updated_at": "2024-05-11T19:13:56.335Z",
      "amount_money": {
        "amount": 3163,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:55.534Z",
          "captured_at": "2024-05-11T19:13:55.678Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Hnz3UGK701rUh9RnPQ815GTxLa4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:55.534Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:56.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3163,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3163,
        "currency": "USD"
      },
      "receipt_number": "RqZk",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/RqZkMaK98ZkH7wFiMcEQ7UYGkhWZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:55.412Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "68BCNnN82BjJPndxwapPbjqmSd62itfypBC6S8w981A6o"
    },
    {
      "id": "piR5U5K9DfurUFGTP6v92zIuAMMZY",
      "created_at": "2024-05-11T19:13:54.616Z",
      "updated_at": "2024-05-11T19:13:55.299Z",
      "amount_money": {
        "amount": 3162,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:54.740Z",
          "captured_at": "2024-05-11T19:13:54.880Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "96Ns3KZVObl8t8YLn60ByBL3Ee4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:54.740Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:55.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3162,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3162,
        "currency": "USD"
      },
      "receipt_number": "piR5",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/piR5U5K9DfurUFGTP6v92zIuAMMZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:54.616Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "NReXsucOinEUQceKpe9EN3GiVrYCM76FYiWaXl5e3yI6o"
    },
    {
      "id": "NkLI3JWpdhGGto2mHPyYTFMN9YKZY",
      "created_at": "2024-05-11T19:13:53.825Z",
      "updated_at": "2024-05-11T19:13:55.216Z",
      "amount_money": {
        "amount": 3161,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:53.950Z",
          "captured_at": "2024-05-11T19:13:54.094Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "BcfxBgPhnnt6roft17psJ4DLne4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:53.950Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:55.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3161,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3161,
        "currency": "USD"
      },
      "receipt_number": "NkLI",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/NkLI3JWpdhGGto2mHPyYTFMN9YKZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:53.825Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "8FFWl9tKLDHxg4DwmCGcbreCsHmgZRScbMKcw9HKAnj6o"
    },
    {
      "id": "tsF94WlGIxcPM5SdT7bnLTnLQbXZY",
      "created_at": "2024-05-11T19:13:52.934Z",
      "updated_at": "2024-05-11T19:13:54.861Z",
      "amount_money": {
        "amount": 3160,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:53.053Z",
          "captured_at": "2024-05-11T19:13:53.197Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "hgVjNrKC8Rq42PNCtOi9mWVDYc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:53.053Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:54.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3160,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3160,
        "currency": "USD"
      },
      "receipt_number": "tsF9",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tsF94WlGIxcPM5SdT7bnLTnLQbXZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:52.934Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "a7qj4eerH0biioyCSNPrZQPlvkal4Aqegrl4FmlCNR85o"
    },
    {
      "id": "pWvl3wEFHm58rfY0sjSxDxs9fe6YY",
      "created_at": "2024-05-11T19:13:52.139Z",
      "updated_at": "2024-05-11T19:13:53.971Z",
      "amount_money": {
        "amount": 3159,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:52.259Z",
          "captured_at": "2024-05-11T19:13:52.407Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "3lCJWUPl2PDfWlZevlANrKS0Ha4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:52.260Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:53.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3159,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3159,
        "currency": "USD"
      },
      "receipt_number": "pWvl",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/pWvl3wEFHm58rfY0sjSxDxs9fe6YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:52.139Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "ceLR83dNUbvvGWXCmVrQxDIX76h9hSGfJndqnL45CXi6o"
    },
    {
      "id": "V2QV2rfhhlBezlAMRpcq2B7ceRUZY",
      "created_at": "2024-05-11T19:13:51.340Z",
      "updated_at": "2024-05-11T19:13:52.927Z",
      "amount_money": {
        "amount": 3158,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:51.459Z",
          "captured_at": "2024-05-11T19:13:51.606Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "zb2Nu48IhPtrL0ECsATsEMkacf4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:51.459Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:52.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3158,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3158,
        "currency": "USD"
      },
      "receipt_number": "V2QV",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/V2QV2rfhhlBezlAMRpcq2B7ceRUZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:51.340Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "lZFjVZvvXYe2aV9EY1e9l5tYQFzh2GKxucaH4ktuiLg6o"
    },
    {
      "id": "hQmllEf4k55khqBZEchRwfxE6LbZY",
      "created_at": "2024-05-11T19:13:50.517Z",
      "updated_at": "2024-05-11T19:13:51.890Z",
      "amount_money": {
        "amount": 3157,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:50.636Z",
          "captured_at": "2024-05-11T19:13:50.786Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "RqKPmCIWixIgoZZii57KXuNlag4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:50.636Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:51.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3157,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3157,
        "currency": "USD"
      },
      "receipt_number": "hQml",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/hQmllEf4k55khqBZEchRwfxE6LbZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:50.517Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "ssiPA6jR1lTHUVf6OvRApSVfctsw975Og7yEHR7awG85o"
    },
    {
      "id": "HR19vkqeBurE6UgZaQ3E0ki4x5IZY",
      "created_at": "2024-05-11T19:13:49.715Z",
      "updated_at": "2024-05-11T19:13:50.852Z",
      "amount_money": {
        "amount": 3156,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:49.842Z",
          "captured_at": "2024-05-11T19:13:49.998Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "RKyn4sunXq00x5pFWdE1TvkYZc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:49.843Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:50.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 122,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3156,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3156,
        "currency": "USD"
      },
      "receipt_number": "HR19",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/HR19vkqeBurE6UgZaQ3E0ki4x5IZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:49.715Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "oTHzHuHRHgKOorrAWQbNu82I663re76neyFIMZZjzLk6o"
    },
    {
      "id": "Ravdfjx6xESz4XZ4ZQzGnhvnZKSZY",
      "created_at": "2024-05-11T19:13:48.912Z",
      "updated_at": "2024-05-11T19:13:50.219Z",
      "amount_money": {
        "amount": 3155,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:49.036Z",
          "captured_at": "2024-05-11T19:13:49.192Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Dze5ShwwnTEWtIYq0eoPxfE3Wc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:49.036Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:50.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3155,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3155,
        "currency": "USD"
      },
      "receipt_number": "Ravd",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/Ravdfjx6xESz4XZ4ZQzGnhvnZKSZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:48.912Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "ABScp9DJhQ88pvz79ch5Fxww61yZx1kex7tKXpkyvqh6o"
    },
    {
      "id": "3bup9yvdER8X1G1A7Tj8jTwyq0XZY",
      "created_at": "2024-05-11T19:13:48.090Z",
      "updated_at": "2024-05-11T19:13:49.812Z",
      "amount_money": {
        "amount": 3154,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:48.212Z",
          "captured_at": "2024-05-11T19:13:48.365Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "RUJw4mdxC8lQKGH9l9CbdBNGwb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:48.212Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:49.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3154,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3154,
        "currency": "USD"
      },
      "receipt_number": "3bup",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/3bup9yvdER8X1G1A7Tj8jTwyq0XZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:48.090Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "PD1DkB8TDBwybnwm9f1GdqzPcj6BInE05oDzjCobfkk6o"
    },
    {
      "id": "V09W9kRnghcuE1nOyBU9o2LkFMAZY",
      "created_at": "2024-05-11T19:13:47.279Z",
      "updated_at": "2024-05-11T19:13:48.802Z",
      "amount_money": {
        "amount": 3153,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:47.402Z",
          "captured_at": "2024-05-11T19:13:47.550Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "Jag7ha1iLZ1AtHX5kU93fqvxyd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:47.402Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:48.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3153,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3153,
        "currency": "USD"
      },
      "receipt_number": "V09W",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/V09W9kRnghcuE1nOyBU9o2LkFMAZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:47.279Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "jypKkZKaV90VPgUko5JLcCzX0VO2UcSfZS86CpsdWhv6o"
    },
    {
      "id": "5Q2as3Kzrw2X5L1AhNCmyAp5SzVZY",
      "created_at": "2024-05-11T19:13:46.437Z",
      "updated_at": "2024-05-11T19:13:47.756Z",
      "amount_money": {
        "amount": 3152,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:46.560Z",
          "captured_at": "2024-05-11T19:13:46.718Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "hiKPi901oBbSM4Hq9Ae1BU12te4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:46.561Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:47.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3152,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3152,
        "currency": "USD"
      },
      "receipt_number": "5Q2a",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5Q2as3Kzrw2X5L1AhNCmyAp5SzVZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:46.437Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "XuAcp4hqEF5U2FqAeadVZLDOvjXfLjlPK3FKxsGW7NJ6o"
    },
    {
      "id": "rjXiJguYvbpOrHmFyWrTqX8yO2VZY",
      "created_at": "2024-05-11T19:13:45.618Z",
      "updated_at": "2024-05-11T19:13:46.628Z",
      "amount_money": {
        "amount": 3151,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:45.744Z",
          "captured_at": "2024-05-11T19:13:45.899Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "lMCfNPw4MXU4C7iKLRR1kaNxCg4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:45.744Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:46.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3151,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3151,
        "currency": "USD"
      },
      "receipt_number": "rjXi",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/rjXiJguYvbpOrHmFyWrTqX8yO2VZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:45.618Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "5LWCxHNXZfQOeWoKfiLozfOXhL0eMSfvkMR5OtR5R9I6o"
    },
    {
      "id": "DbfJ21cBIlQOrNRs6rJVrXMQmSNZY",
      "created_at": "2024-05-11T19:13:44.696Z",
      "updated_at": "2024-05-11T19:13:46.143Z",
      "amount_money": {
        "amount": 3150,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:44.819Z",
          "captured_at": "2024-05-11T19:13:44.966Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "LBhsg1t0l3LJP7LczQ9QRQrWLa4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:44.819Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:46.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3150,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3150,
        "currency": "USD"
      },
      "receipt_number": "DbfJ",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/DbfJ21cBIlQOrNRs6rJVrXMQmSNZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:44.696Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "0y8xYhnuUYZeFy1iop6s3nAFBdr4TUyUHFU6MKgpWlo6o"
    },
    {
      "id": "xupjmk35wxWDE5Cl4QwP3ywpQaLZY",
      "created_at": "2024-05-11T19:13:43.878Z",
      "updated_at": "2024-05-11T19:13:45.585Z",
      "amount_money": {
        "amount": 3149,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:44.004Z",
          "captured_at": "2024-05-11T19:13:44.154Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "JgJ6FL6dOHytcNtoXLjBJVa2wc4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:44.005Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:45.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3149,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3149,
        "currency": "USD"
      },
      "receipt_number": "xupj",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/xupjmk35wxWDE5Cl4QwP3ywpQaLZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:43.878Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "fQJLi0wEq6eOVrHPApIzuzggBVyb1AtiXbZfwMK94yG6o"
    },
    {
      "id": "jHtFeMJScLhS6SlY7ktNfVKYV7QZY",
      "created_at": "2024-05-11T19:13:43.076Z",
      "updated_at": "2024-05-11T19:13:44.998Z",
      "amount_money": {
        "amount": 3148,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:43.198Z",
          "captured_at": "2024-05-11T19:13:43.354Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "54zfHQAsW8OgtHzUGXBZFYLYgf4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:43.198Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:44.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3148,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3148,
        "currency": "USD"
      },
      "receipt_number": "jHtF",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/jHtFeMJScLhS6SlY7ktNfVKYV7QZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:43.076Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "sddYRENzqqOZSqPLF0cgPwo65cY2TiQwjAyAp2E3rwl6o"
    },
    {
      "id": "5uXRf12ynhgSl1mx1vwCRQabc1OZY",
      "created_at": "2024-05-11T19:13:42.292Z",
      "updated_at": "2024-05-11T19:13:43.768Z",
      "amount_money": {
        "amount": 3147,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:42.415Z",
          "captured_at": "2024-05-11T19:13:42.561Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "9qvBjQdtEzEn0MfK4UvylTOz7a4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:42.415Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:43.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3147,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3147,
        "currency": "USD"
      },
      "receipt_number": "5uXR",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/5uXRf12ynhgSl1mx1vwCRQabc1OZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:42.292Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "sISeKityOWnKsD2502YZqqtfx5EKkh6Dge1P5bmOWR45o"
    },
    {
      "id": "B04lFjXIPOIMIcIwycIBRl9qdGDZY",
      "created_at": "2024-05-11T19:13:41.514Z",
      "updated_at": "2024-05-11T19:13:42.940Z",
      "amount_money": {
        "amount": 3146,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:41.636Z",
          "captured_at": "2024-05-11T19:13:41.783Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "laH42l49odAN9Iid1uAumaOioe4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:41.636Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:42.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3146,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3146,
        "currency": "USD"
      },
      "receipt_number": "B04l",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/B04lFjXIPOIMIcIwycIBRl9qdGDZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:41.514Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "bRwx1EFLUD4IaW6VkNd8aM2FcRYn3vQKhCjPQv7KMvN6o"
    },
    {
      "id": "7zTEIqSprIZUkO32mSCR9jYQlVZZY",
      "created_at": "2024-05-11T19:13:40.718Z",
      "updated_at": "2024-05-11T19:13:41.646Z",
      "amount_money": {
        "amount": 3145,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:40.840Z",
          "captured_at": "2024-05-11T19:13:40.982Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "LzaAqdjNkfODlKAjmeAyaDqfYf4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:40.840Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:41.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3145,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3145,
        "currency": "USD"
      },
      "receipt_number": "7zTE",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/7zTEIqSprIZUkO32mSCR9jYQlVZZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:40.718Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "IVItS5dZHxsn1mRTWiwyDmL1ZOvUoKrItPVKmf2Apvu6o"
    },
    {
      "id": "tAp4fwoM4LuZFN9j1hhJtOAZmQeZY",
      "created_at": "2024-05-11T19:13:39.891Z",
      "updated_at": "2024-05-11T19:13:41.480Z",
      "amount_money": {
        "amount": 3144,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:40.015Z",
          "captured_at": "2024-05-11T19:13:40.162Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "xqckieQSDYWhik0fVPTCyBXB1c4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:40.015Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:41.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3144,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3144,
        "currency": "USD"
      },
      "receipt_number": "tAp4",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/tAp4fwoM4LuZFN9j1hhJtOAZmQeZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:39.891Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "CDCIU7AX3KZzvDeGUXRt6YdkD2ALgtRFxHfkC9kojA16o"
    },
    {
      "id": "NaeY3IA9Umd81NbCvFFdQZi8uxGZY",
      "created_at": "2024-05-11T19:13:39.105Z",
      "updated_at": "2024-05-11T19:13:40.880Z",
      "amount_money": {
        "amount": 3143,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:39.226Z",
          "captured_at": "2024-05-11T19:13:39.372Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "bVHi90qemmUo8HHGiNNME70F5h4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:39.226Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:40.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3143,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3143,
        "currency": "USD"
      },
      "receipt_number": "NaeY",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/NaeY3IA9Umd81NbCvFFdQZi8uxGZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:39.105Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "wpTfeOcWVmGVLHD1CykYseynwoe8vXWcuuSaRrMys8V6o"
    },
    {
      "id": "fnm1kcp1k2UGuZH2EZ4chazzCR7YY",
      "created_at": "2024-05-11T19:13:38.314Z",
      "updated_at": "2024-05-11T19:13:39.597Z",
      "amount_money": {
        "amount": 3142,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:38.436Z",
          "captured_at": "2024-05-11T19:13:38.578Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "LZPnLe29hfDfFukYAsVOxfPcFa4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:38.437Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:39.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3142,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3142,
        "currency": "USD"
      },
      "receipt_number": "fnm1",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/fnm1kcp1k2UGuZH2EZ4chazzCR7YY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:38.314Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "u7w7LY9ATpaDWtEflEm3JmB1zmkplYS5nYTTYvGT5JW6o"
    },
    {
      "id": "3TefNvdx5z3JQoCJtyeHn3SuD0EZY",
      "created_at": "2024-05-11T19:13:37.515Z",
      "updated_at": "2024-05-11T19:13:38.391Z",
      "amount_money": {
        "amount": 3141,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:37.639Z",
          "captured_at": "2024-05-11T19:13:37.803Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "P9ueXevs0YF1zCvvKW3mdayWba4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:37.639Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:38.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3141,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3141,
        "currency": "USD"
      },
      "receipt_number": "3Tef",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/3TefNvdx5z3JQoCJtyeHn3SuD0EZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:37.515Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "Jkbl7CMij6dtAvBPOTzFRzEvqqVWDt1byn0qjTdeKzr6o"
    },
    {
      "id": "Lj7wLnTrGf96UCJ0jbQzTu8wM9cZY",
      "created_at": "2024-05-11T19:13:36.711Z",
      "updated_at": "2024-05-11T19:13:37.630Z",
      "amount_money": {
        "amount": 3140,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:36.833Z",
          "captured_at": "2024-05-11T19:13:36.975Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "B2ae0C20JVBe2HSKJgwkvxLK8e4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:36.833Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:37.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3140,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3140,
        "currency": "USD"
      },
      "receipt_number": "Lj7w",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/Lj7wLnTrGf96UCJ0jbQzTu8wM9cZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:36.711Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "8ibPPlRwZ0rf8OdBp8qR2ugCGOxAE2kz0hGw0xIBwT85o"
    },
    {
      "id": "d2sQSQW8AaX9ZkkoVb37lJrp2kEZY",
      "created_at": "2024-05-11T19:13:35.915Z",
      "updated_at": "2024-05-11T19:13:37.629Z",
      "amount_money": {
        "amount": 3139,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:36.036Z",
          "captured_at": "2024-05-11T19:13:36.189Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "tu5pobIk85HmwQ8h5fiQ1nGaKd4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:36.036Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:37.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3139,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3139,
        "currency": "USD"
      },
      "receipt_number": "d2sQ",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/d2sQSQW8AaX9ZkkoVb37lJrp2kEZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:35.915Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "yih8dw3JXb2ARGVC1P0T2sGBQiRMWpyw0eBmWgDw4Mm6o"
    },
    {
      "id": "bVCX0mwYMVKm0zRhDRpHNdf1kYEZY",
      "created_at": "2024-05-11T19:13:35.125Z",
      "updated_at": "2024-05-11T19:13:36.536Z",
      "amount_money": {
        "amount": 3138,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:35.247Z",
          "captured_at": "2024-05-11T19:13:35.393Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "XFQ4wo1gxjmnlxuo42tHgTGd2g4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:35.247Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:36.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3138,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3138,
        "currency": "USD"
      },
      "receipt_number": "bVCX",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/bVCX0mwYMVKm0zRhDRpHNdf1kYEZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:35.125Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "w6yTvbDCL8qOrj56SRlFpeGkEkMwOcnlDhhEBkAONof6o"
    },
    {
      "id": "bNejkPSVmZg6JEAjdZ5Ug8ayMqMZY",
      "created_at": "2024-05-11T19:13:34.335Z",
      "updated_at": "2024-05-11T19:13:35.498Z",
      "amount_money": {
        "amount": 3137,
        "currency": "USD"
      },
      "status": "COMPLETED",
      "delay_duration": "PT168H",
      "source_type": "CARD",
      "card_details": {
        "status": "CAPTURED",
        "card": {
          "card_brand": "VISA",
          "last_4": "5858",
          "exp_month": 5,
          "exp_year": 2026,
          "fingerprint": "sq-1-mzz3vE0RTtj6Nxfpv8kHBKGgDw74TBOFWf_Wof8lToLm2jOrmrFCnX2uCQ2RZ-cdjg",
          "card_type": "CREDIT",
          "prepaid_type": "NOT_PREPAID",
          "bin": "453275"
        },
        "entry_method": "KEYED",
        "cvv_status": "CVV_ACCEPTED",
        "avs_status": "AVS_ACCEPTED",
        "statement_description": "SQ *DEFAULT TEST ACCOUNT",
        "card_payment_timeline": {
          "authorized_at": "2024-05-11T19:13:34.456Z",
          "captured_at": "2024-05-11T19:13:34.604Z"
        }
      },
      "location_id": "LT9QVCXSARE9G",
      "order_id": "ZArtdROxObnZKNXsKnt7pjBFNb4F",
      "risk_evaluation": {
        "created_at": "2024-05-11T19:13:34.456Z",
        "risk_level": "NORMAL"
      },
      "processing_fee": [
        {
          "effective_at": "2024-05-11T21:13:35.000Z",
          "type": "INITIAL",
          "amount_money": {
            "amount": 121,
            "currency": "USD"
          }
        }
      ],
      "total_money": {
        "amount": 3137,
        "currency": "USD"
      },
      "approved_money": {
        "amount": 3137,
        "currency": "USD"
      },
      "receipt_number": "bNej",
      "receipt_url": "https://squareupsandbox.com/receipt/preview/bNejkPSVmZg6JEAjdZ5Ug8ayMqMZY",
      "delay_action": "CANCEL",
      "delayed_until": "2024-05-18T19:13:34.335Z",
      "application_details": {
        "square_product": "ECOMMERCE_API",
        "application_id": "sandbox-sq0idb-kUkgPZsjXviQduph8QQWYA"
      },
      "version_token": "GNgfGTgz2kTCZ1HX4p2mZawuDXT07N2KP9rp67u88Cs6o"
    }
  ],
  "cursor": "eyJjcmVhdGVkQXQiOjE3MTU0NTQ4MTQzMzUsImlkIjoiYk5lamtQU1ZtWmc2SkVBamRaNVVnOGF5TXFNWlkifQ"
}

test_result = parse_api_call(test_set)
print(len(test_result))