preprints = [
]
published = [
    {
        "title": "Commit-and-Prove System for Vectors and Applications to Threshold Signing",
        "coauthors": "Anja Lehmann",
        "venue": "PKC'25",
        "year": 2025,
        "eprint": "https://eprint.iacr.org/2025/355",
        "published": "https://link.springer.com/chapter/10.1007/978-3-031-91826-1_7",
        "abstract": "Multi-signatures allow to combine several individual signatures into a compact one and verify it against a short aggregated key. Compared to threshold signatures, multi-signatures enjoy non-interactive key generation but give up on the threshold-setting. Recent works by Das et al.(CCS'23) and Garg et al.(S&P'24) show how multi-signatures can be turned into schemes that enable efficient verification when an ad hoc threshold &mdash; determined only at verification &mdash; is satisfied. This allows to keep the simple key generation of multi-signatures and support flexible threshold settings in the signing process later on. Both works use the same idea of combining BLS multi-signatures with inner-product proofs over committed keys. Das et al. give a somewhat generic proof from both building blocks, which we show to be flawed, whereas Garg et al. give a direct proof for the combined construction in the algebraic group model."

    },
    {
        "title": "Privacy-Preserving Multi-Signatures: Generic Techniques and Constructions Without Pairings",
        "coauthors": "Calvin Abou Haidar, Dipayan Das, Anja Lehmann, and Octavio Perez Kempner",
        "venue": "PKC'25",
        "year": 2025,
        "eprint": "https://eprint.iacr.org/2025/335",
        "published": "https://link.springer.com/chapter/10.1007/978-3-031-91823-0_3",
        "abstract": "Multi-signatures allow a set of parties to produce a single signature for a common message by combining their individual signatures. The result can be verified using the aggregated public key that represents the group of signers. Very recent work by Lehmann and Özbay (PKC'24) studied the use of multi-signatures for ad-hoc privacy-preserving group signing, formalizing the notion of multi-signatures with probabilistic yet verifiable key aggregation. Moreover, they proposed new BLS-type multi-signatures, allowing users holding a long-term key pair to engage with different groups, without the aggregated key leaking anything about the corresponding group. This enables key-reuse across different groups in a privacy-preserving way. Unfortunately, their technique cannot be applied to Schnorr-type multi-signatures, preventing state-of-the-art multi-signatures to benefit from those privacy features."
    },
    {
        "title": "Stronger Security for Threshold Blind Signatures",
        "coauthors": "Anja Lehmann and Phillip Nazarian",
        "venue": "EUROCRYPT'25",
        "year": 2025,
        "eprint": "https://eprint.iacr.org/2025/353",
        "published": "https://link.springer.com/chapter/10.1007/978-3-031-91124-8_12",
        "talk": "https://www.youtube.com/watch?v=0DoLLBDi0k4&t=1041s",
        "abstract": "Blind signatures allow a user to obtain a signature from an issuer in a privacy-preserving way: the issuer neither learns the signed message, nor can link the signature to its issuance. The threshold version of blind signatures further splits the secret key among n issuers, and requires the user to obtain at least t of signature shares in order to derive the final signature. Security should then hold as long as at most t-1 issuers are corrupt. Security for blind signatures is expressed through the notion of one-more unforgeability and demands that an adversary must not be able to produce more signatures than what is considered trivial after its interactions with the honest issuer(s). While one-more unforgeability is well understood for the single-issuer setting, the situation is much less clear in the threshold case: due to the blind issuance, counting which interactions can yield a trivial signature is a challenging task. Existing works bypass that challenge by using simplified models that do not fully capture the expectations of the threshold setting. In this work, we study the security of threshold blind signatures, and propose a framework of one-more unforgeability notions where the adversary can corrupt (c &lt t) issuers. Our model is generic enough to capture both interactive and non-interactive protocols, and it provides a set of natural properties with increasingly stronger guarantees, giving the issuers gradually more control over how their shares can be combined. As a point of comparison, we reconsider the existing threshold blind signature models and show that their security guarantees are weaker and less clearly comprehensible than they seem. We then re-assess the security of existing threshold blind signature schemes &mdash; BLS-based and Snowblind &mdash; in our framework, and show how to lift them to provide stronger security."
    },
    {
        "title": "OPPID: Single Sign-On with Oblivious Pairwise Pseudonyms",
        "coauthors": "Maximilian Kroschewski and Anja Lehmann",
        "venue": "To appear at PETS'25",
        "year": 2025,
        "eprint": "https://eprint.iacr.org/2024/1124",
        "published": "https://petsymposium.org/popets/2025/popets-2025-0080.php",
        "abstract": "Single Sign-On (SSO) allows users to conveniently authenticate to many Relying Parties (RPs) through a central Identity Provider (IdP). SSO supports unlinkable authentication towards the RPs via pairwise pseudonyms, where the IdP assigns the user an RP-specific pseudonym. This feature has been rolled out prominently within Apple's SSO service. While establishing unlinkable identities provides privacy towards RPs, it actually emphasizes the main privacy problem of SSO: with every authentication request, the IdP learns the RP that the user wants to access. Solutions to overcome this limitation exist, but either assume users to behave honestly or require them to manage long-term cryptographic keys. In this work, we propose the first SSO system that can provide such pseudonymous authentication in an unobservable yet strongly secure and convenient manner. That is, the IdP blindly derives the user's pairwise pseudonym for the targeted RP without learning the RP's identity and without requiring key material handled by the user. We formally define the desired security and privacy properties for such unlinkable, unobservable, and strongly secure SSO. In particular, our model includes the often neglected RP authentication: the IdP typically wants to limit its services to registered RPs only and thus must be able to (blindly) verify that it issues the token and pseudonym to such a registered RP. We propose a simple construction that combines signatures with efficient proofs-of-knowledge with a blind, yet verifiable, evaluation of the Hashed-Diffie-Hellman PRF. We prove the security of our construction and demonstrate its efficiency through a prototypical implementation, which requires a running time of 2-12ms per involved party."
    },
    {
        "title": "Multi-Signatures for Ad-hoc and Privacy-Preserving Group Signing",
        "coauthors": "Anja Lehmann",
        "venue": "PKC'24",
        "year": 2024,
        "eprint": "https://eprint.iacr.org/2023/1884",
        "published": "https://link.springer.com/chapter/10.1007/978-3-031-57718-5_7",
        "talk": "https://www.youtube.com/watch?v=Wdhlp2NKZDA&t=2143s",
        "abstract": "Multi-signatures allow to combine individual signatures from different signers on the same message into a short aggregated signature. Newer schemes further allow to aggregate the individual public keys, such that the combined signature gets verified against a short aggregated key. This makes them a versatile alternative to threshold or distributed signatures: the aggregated key can serve as group key, and signatures under that key can only be computed with the help of all signers. What makes multi-signatures even more attractive is their simple key management, as users can re-use the same secret key in several and ad-hoc formed groups. In that context, it will be desirable to not sacrifice privacy as soon as keys get re-used and ensure that users are not linkable across groups. In fact, when multi-signatures with key aggregation were proposed, it was claimed that aggregated keys hide the signers' identities or even the fact that it is a combined key at all. In our work, we show that none of the existing multi-signature schemes provide these privacy guarantees when keys get re-used in multiple groups. This is due to the fact that all known schemes deploy deterministic key aggregation. To overcome this limitation, we propose a new variant of multi-signatures with probabilistic yet verifiable key aggregation. We formally define the desirable privacy and unforgeability properties in the presence of key re-use. This also requires to adapt the unforgeability model to the group setting, and ensure that key-reuse does not weaken the expected guarantees. We present a simple BLS-based scheme that securely realizes our strong privacy and security guarantees. We also formalize and investigate the privacy that is possible by deterministic schemes, and prove that existing schemes provide the advertised privacy features as long as one public key remains secret."
    },
    {
        "title": "Blacklisting Based Anonymous Authentication Scheme for Sharing Economy",
        "coauthors": "Albert Levi",
        "venue": "IEEE TDSC'23",
        "year": 2023,
        "published": "https://ieeexplore.ieee.org/document/10089488",
        "abstract": "Authentication and blacklisting mechanisms have a key role for service providers to deliver the service to correct users through digital channels. Nevertheless, there always have been concerns about privacy of the users against such mechanisms. The conditional anonymity concept is proposed as a remedy to these concerns. A recent approach in the literature for conditional anonymity is blacklistable anonymous credentials, which allows service providers to blacklist users for an authentication session without identifying the user. In this paper, we improve user anonymity in conditionally anonymous schemes using two complementary mechanisms. First, we define whitelisting property for blacklistable anonymous credentials and give a construction of this scheme. The whitelisting property can be used to unlink an honestly behaved authentication session from the user. Second, we propose an extension of this scheme for a particular use case, sharing economy services. This scheme allows a service provider to blacklist a user only if the user have not returned the shared asset in due time. We benchmark the performance of our schemes by comparing them with the rival schemes. Our experiments show that both of our scheme have comparable performance to previous works."
    }
]