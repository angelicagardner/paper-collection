---
title: "Bitcoin: A Peer-to-Peer Electronic Cash System"
labels: "cryptocurrency"
year: 2008
---

# Bitcoin: A Peer-to-Peer Electronic Cash System

**Author(s):** Satoshi Nakamoto

**Paper URL:** https://bitcoin.org/bitcoin.pdf

**Pages:** 8

**Summary:** This paper proposes a decentralized digital currency that allows people to send payments directly to each other without relying on banks. It introduces a public ledger called the blockchain and uses a consensus mechanism called proof-of-work to prevent double-spending and ensure transaction security. The suggested system removes the need for trusted third parties and creates a limited-supply, peer-to-peer electronic cash network.

## Sections Summary

### `1. Introduction`

- Current internet commerce relies on "trusted" financial institutions that act as intermediaries

- This paper argues we need a system based on cryptographic proof so two parties can transact directly without a middleman.

- To prevent "double-spending" without a central authority, the paper proposes a distributed peer-to-peer server that generates a public, chronological record of transactions secured by the network's collective CPU power.
  
### `2. Transactions`

- An electronic coin is defined as a chain of digital signatures where owners transfer value by signing a hash of the previous transaction, though this technical verification alone cannot prove that an owner hasn't already spent the coin elsewhere.

- Relying on a central authority (a "mint") to prevent double-spending creates a single point of failure where the fate of the entire system depends on the company running it.

- To eliminate the central authority, all transactions must be publicly announced so that the entire network can agree on a single, chronological history of transactions based on which one the majority of nodes received first.

### `3. Timestamp Server`

- The system creates a record of when data existed by taking a hash of a block of items and widely publishing it.

- Each new timestamp incorporates the previous timestamp within its own hash, creating a continuous chain where every additional block strengthens and validates the chronological order of all preceding entries.

- Bitcoin uses this "Hash Chain" to ensure that once a "timestamp" (block) is published, the history cannot be changed without changing every subsequent hash in the system.

### `4. Proof-of-Work`

- To implement the timestamp server in a Peer-to-Peer system (where there is no leader), a proof-of-work system is needed.

- To prevent fraudulent voting from taking over the network by simply creating thousands of fake identities (a "Sybil attack"), the paper establishes a "one-CPU-one-vote" system where nodes must prove they expended actual energy to validate a block.

- Finding a valid block requires solving a difficult mathematical puzzle which makes the chain immutable because an attacker would have to redo the work for every subsequent block to change a single past transaction (i.e. impossible as long as honest nodes control the majority of CPU power).

### `5. Network`

- New transactions are broadcast to all nodes, and each node collects these into a candidate block.

- Every node works on finding the difficult Proof-of-Work for its block; the first node to solve the puzzle broadcasts its successful block to the entire network.

- Nodes accept the block only if all transactions inside it are valid and not already spent.

- Nodes always consider the longest chain (with the most proof-of-work) to be the correct one and will switch to a longer branch if it appears, ensuring the network eventually converges on a single history.

### `6. Incentive`

- The incentive answers why anyone would spend on electricity and hardware to secure a network they don't own.

- The first transaction in every block is a special transaction that creates new coins for the node that found the block (mining).

- Once the total supply is reached, the incentive shifts to transaction fees.

- The incentive is designed to make attacking the network less profitable than following the rules. 

### `7. Reclaiming Disk Space`

- Once a transaction is "buried" under enough blocks and its coins are spent, the raw data for that transaction is no longer strictly needed to verify future blocks and can be discarded to save space.

### `8. Simplified Payment Verification`

- "Lightweight" users don't need to download the entire multi-gigabyte blockchain, they only need to keep the 80-byte block headers of the longest chain to verify that a transaction has been accepted by the network.

- SPV is less secure than running a full node because you are trusting that the "Longest Chain" you see is the honest one. Therefore, it's recommended in the paper that businesses that receive frequent payments run their own nodes.

### `9. Combining and Splitting Value`

- To avoid the inefficiency of sending 100 separate transactions for small amounts, the protocol allows a single transaction to contain multiple inputs and outputs.

- History is decoupled so a user never needs to download or extract the complete, standalone history of every single branch to verify their own current transaction. Since each is independent, many transactions can be processed in parallel.

### `10. Privacy`

- In traditional banking the ledger is kept private and only the parties involved see the data. In Bitcoin, the ledger is public.

- While the entire network can see that an amount of money moved from one address to another, they cannot see who those addresses belong to because public keys are kept anonymous.

### `11. Calculations`

- This section is an example of Formal Verification in distributed systems.

- It mathematically proves that the cost of the electricity and hardware needed to attempt an attack is higher than the expected gain.

## Questions/Discussion Points

- Gap between Satoshi's vision and the current industry reality: 
	- Many users don't manage their own private keys but keep their Bitcoin on a centralized exchange or a managed wallet, which is basically using a "trusted third party"?
- Central banks can print more money which devalues the currency you already hold. Bitcoin solves this with a fixed supply (21 million). Bitcoin was designed to solve monetary debasement (printing money), not market fluctuations (people changing their minds about what it's worth). So the bitcoin is still vulnerable to wealth decreasing (because of value fall on stock market).
- Could be interesting to read "The Bitcoin Backbone Protocol" or a paper on Ethereum's architecture as follow-up.
