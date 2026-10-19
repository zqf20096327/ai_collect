# Closure SDK

Compare two ordered streams of records and find what is missing, what moved,
and where, using the geometry of rotations.

![Two compositions of the same records, unrolled from the three-sphere and compared mark by mark](assets/closure-records.webp)

```bash
cargo install --git https://github.com/faltz009/Closure-SDK
closure identity source.jsonl target.jsonl
```

`closure identity` lists every missing and moved record with its position in
both files and its payload, writes a JSON report, and exits with status 2 when
the files differ. Use it to reconcile pipeline outputs, exports and replicas.

## How it works

Every record becomes a rotation, a unit quaternion on the three-sphere S³, and
a stream is the product of its records in order: one point of 32 bytes,
whatever the stream's length. A copy of the same records in the same order
lands on the same point. Quaternions keep order (ab ≠ ba), grouping
((ab)c = a(bc)) and size (|ab| = |a||b|), so a change of size ε anywhere in a
stream moves the result by exactly ε, at every position.

When two streams differ, a binary search on their running products finds
where they part, and a two-pointer walk (Gilgamesh) names every incident from
there in one linear pass: **missing** when a record is on one side only,
**moved** when it is on both sides in different places. The two kinds are
different directions on the sphere: a missing record g leaves a gap g − 1 with
a real part, and a record a moved past a block M leaves aM − Ma, whose real
part is zero.

For live streams, Enkidu holds each unmatched record's slot open for one cycle
of a shared counter. A slot that closes empty is missing, and a counterpart
that arrives later turns it into a move.

## Benchmarks

One million JSON records with 10 dropped, 10 inserted, 10 moved and 10
changed, every report scored against the known answer, on an Intel i5-10400F.

| Method | 1 thread | 12 threads | Exact |
|---|---:|---:|:-:|
| **Closure**, unhashed | **144 ms** | **74 ms** | **yes** |
| **Closure**, SHA-256 | 854 ms | 174 ms | **yes** |
| Myers diff in Rust (`similar`) | 192 ms | — | no: a move is a deletion plus an insertion |
| GNU diff 3.12 (files) | 325 ms | — | no: a move is a deletion plus an insertion |
| Hash-map count | 194 ms | — | no: moves are invisible |

Closure is exact in all 120 measured runs. The method and every number are in
[benches/README.md](benches/README.md).

## The CLI

| Command | What it does |
|---|---|
| `closure identity a b` | Reconciles two complete files: JSONL, CSV or text |
| `closure observer a b` | Watches two live streams and diagnoses them when their summaries part |
| `closure seeker a b` | Classifies every record of two live streams as it arrives |

Inputs can be files, named pipes or `-` for stdin. Details are in
[CLOSURE_CLI.md](CLOSURE_CLI.md).

## The library

```rust
use closure_sdk::{gilgamesh, Seer};

// Detect: one constant-size summary per stream.
let (mut a, mut b) = (Seer::new(), Seer::new());
a.ingest_many(&source);
b.ingest_many(&target);
if !a.compare(&b).coherent {
    // Diagnose: every incident, with positions and payload.
    for incident in gilgamesh(&source, &target) {
        println!("{} {:?} → {:?}", incident.kind, incident.source_index, incident.target_index);
    }
}
```

Records are hashed onto the sphere with SHA-256; points you already have
(rotations, phases, musical intervals) compose as they are. The full
reference and the theory are in [CLOSURE_SDK.md](CLOSURE_SDK.md), and runnable
examples are in `examples/`.

## Tests

```bash
cargo test --release --locked
```

## Support

Independent research, done on personal time and released for free.

| Method | Address |
|---|---|
| Ko-fi | [ko-fi.com/waltersilva](https://ko-fi.com/waltersilva) |
| BTC | `155jaKugGGhdwX2Dp55bfHWpWbWD3Gr3PG` |
| ETH (ERC-20) | `0x31f0253180b03c16a0aa2d7091311d7363ef22a4` |
| SOL | `HdGFaL6A8z8AetnyPn6vKPU4QJGaSHBtoqPK32qbe6wV` |
| PIX (Brazil) | `walter.h057@gmail.com` |

## License

AGPL-3.0-only
