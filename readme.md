# Chia Offer Generator
This allow to offer files for selling or buying CAT token.
It allow to set up the number of offer to generate to match the total requested amount.

## Usage
Edit the data.json

```
{
  "walletFingerprint": "1234567789", // Finger print of the wallet to use
  "nbTogenerate": 20, // Number of offer to generate
  "offerWalletID": 7, // Wallet ID to offer
  "requestWalletID": 1, // Wallet ID to request
  "requestAmount": 4, // Total request amount
  "price": 0.00001, // Start price
  "increment": 2 // Total increment in percent (2 = 2%) to increment between the first and the last offer.
}
```

In this example we generate 20 offer to sell SBX at starting price 0.00001. Each offer will request 4/20 = 0.2 XCH. The amount of SBX will be between the price of 0.00001 and 0.0000102

## Warning
It is possible that the offer will not all be generated if you don't have enough coin to use.