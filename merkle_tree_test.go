package merkle_tree_bench

import (
	"bytes"
	"crypto/rand"
	"crypto/sha256"
	"testing"

	cbergoon "github.com/cbergoon/merkletree"
	txaty "github.com/txaty/go-merkletree"
	wealdtech "github.com/wealdtech/go-merkletree"
)

const (
	treeDepth = 17
	benchSize = 1 << treeDepth
)

type wealdtechHashType struct{}

func (w wealdtechHashType) Hash(data []byte) []byte {
	h := sha256.New()
	if _, err := h.Write(data); err != nil {
		panic(err)
	}

	return h.Sum(nil)
}

type dataBlock struct {
	data []byte
}

func newDataBlock() dataBlock {
	randBytes := make([]byte, 64)
	_, err := rand.Read(randBytes)
	if err != nil {
		panic(err)
	}
	return dataBlock{data: randBytes}
}

func (d dataBlock) Serialize() ([]byte, error) {
	return d.data, nil
}

func (d dataBlock) CalculateHash() ([]byte, error) {
	h := sha256.New()
	if _, err := h.Write(d.data); err != nil {
		return nil, err
	}

	return h.Sum(nil), nil
}

func (d dataBlock) Equals(other cbergoon.Content) (bool, error) {
	if other, ok := other.(dataBlock); ok {
		return bytes.Equal(d.data, other.data), nil
	}
	return false, nil
}

func Benchmark_txatyMerkleTreeProofGenAll(b *testing.B) {
	dataBlocks := make([]txaty.DataBlock, benchSize)
	for i := 0; i < benchSize; i++ {
		dataBlocks[i] = newDataBlock()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := txaty.New(nil, dataBlocks)
		if err != nil {
			b.Fatal(err)
		}
		for i := 0; i < benchSize; i++ {
			_ = tree.Proofs[i]
		}
		_ = tree.Root
	}
}

func Benchmark_txatyMerkleTreeProofGenParallelAll(b *testing.B) {
	dataBlocks := make([]txaty.DataBlock, benchSize)
	for i := 0; i < benchSize; i++ {
		dataBlocks[i] = newDataBlock()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := txaty.New(&txaty.Config{RunInParallel: true}, dataBlocks)
		if err != nil {
			b.Fatal(err)
		}
		for i := 0; i < benchSize; i++ {
			_ = tree.Proofs[i]
		}
		_ = tree.Root
	}
}

func Benchmark_cbergoonMerkleTreeProofGenAll(b *testing.B) {
	testContents := make([]cbergoon.Content, benchSize)
	for i := 0; i < benchSize; i++ {
		testContents[i] = newDataBlock()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := cbergoon.NewTree(testContents)
		if err != nil {
			b.Fatal(err)
		}
		for _, content := range testContents {
			_, _, err := tree.GetMerklePath(content)
			if err != nil {
				b.Fatal(err)
			}
		}
		tree.MerkleRoot()
	}
}

func Benchmark_wealdtechMerkleTreeProofGenAll(b *testing.B) {
	data := make([][]byte, benchSize)
	for i := 0; i < benchSize; i++ {
		data[i] = newDataBlock().data
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := wealdtech.NewUsing(data, wealdtechHashType{}, nil)
		if err != nil {
			b.Fatal(err)
		}
		for _, d := range data {
			_, err := tree.GenerateProof(d)
			if err != nil {
				b.Fatal(err)
			}
		}
		_ = tree.Root()
	}
}

func Benchmark_txatyMerkleTreeProofGenSingle(b *testing.B) {
	dataBlocks := make([]txaty.DataBlock, benchSize)
	for i := 0; i < benchSize; i++ {
		dataBlocks[i] = newDataBlock()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := txaty.New(&txaty.Config{Mode: txaty.ModeTreeBuild}, dataBlocks)
		if err != nil {
			b.Fatal(err)
		}
		_, err = tree.Proof(dataBlocks[benchSize/2])
		if err != nil {
			b.Fatal(err)
		}
	}
}

func Benchmark_txatyMerkleTreeProofGenParallelSingle(b *testing.B) {
	dataBlocks := make([]txaty.DataBlock, benchSize)
	for i := 0; i < benchSize; i++ {
		dataBlocks[i] = newDataBlock()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := txaty.New(&txaty.Config{Mode: txaty.ModeTreeBuild, RunInParallel: true}, dataBlocks)
		if err != nil {
			b.Fatal(err)
		}
		_, err = tree.Proof(dataBlocks[benchSize/2])
		if err != nil {
			b.Fatal(err)
		}
	}
}

func Benchmark_cbergoonMerkleTreeProofGenSingle(b *testing.B) {
	testContents := make([]cbergoon.Content, benchSize)
	for i := 0; i < benchSize; i++ {
		testContents[i] = newDataBlock()
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := cbergoon.NewTree(testContents)
		if err != nil {
			b.Fatal(err)
		}
		_, _, err = tree.GetMerklePath(testContents[benchSize/2])
		if err != nil {
			b.Fatal(err)
		}
	}
}

func Benchmark_wealdtechMerkleTreeProofGenSingle(b *testing.B) {
	data := make([][]byte, benchSize)
	for i := 0; i < benchSize; i++ {
		data[i] = newDataBlock().data
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		tree, err := wealdtech.NewUsing(data, wealdtechHashType{}, nil)
		if err != nil {
			b.Fatal(err)
		}
		_, err = tree.GenerateProof(data[benchSize/2])
		if err != nil {
			b.Fatal(err)
		}
	}
}

func Benchmark_txatyMerkleTreeVerify(b *testing.B) {
	dataBlocks := make([]txaty.DataBlock, benchSize)
	for i := 0; i < benchSize; i++ {
		dataBlocks[i] = newDataBlock()
	}
	tree, err := txaty.New(&txaty.Config{Mode: txaty.ModeTreeBuild}, dataBlocks)
	if err != nil {
		b.Fatal(err)
	}
	proof, err := tree.Proof(dataBlocks[benchSize/2])
	if err != nil {
		b.Fatal(err)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		ok, err := tree.Verify(dataBlocks[benchSize/2], proof)
		if err != nil {
			b.Fatal(err)
		}
		if !ok {
			b.Fatal("verification failed")
		}
	}
}

func Benchmark_cbergoonMerkleTreeVerify(b *testing.B) {
	testContents := make([]cbergoon.Content, benchSize)
	for i := 0; i < benchSize; i++ {
		testContents[i] = newDataBlock()
	}
	tree, err := cbergoon.NewTree(testContents)
	if err != nil {
		b.Fatal(err)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		ok, err := tree.VerifyContent(testContents[benchSize/2])
		if err != nil {
			b.Fatal(err)
		}
		if !ok {
			b.Fatal("verification failed")
		}
	}
}

func Benchmark_wealdtechMerkleTreeVerify(b *testing.B) {
	data := make([][]byte, benchSize)
	for i := 0; i < benchSize; i++ {
		data[i] = newDataBlock().data
	}
	tree, err := wealdtech.NewUsing(data, wealdtechHashType{}, nil)
	if err != nil {
		b.Fatal(err)
	}
	proof, err := tree.GenerateProof(data[benchSize/2])
	if err != nil {
		b.Fatal(err)
	}
	b.ResetTimer()
	for i := 0; i < b.N; i++ {
		ok, err := wealdtech.VerifyProofUsing(data[benchSize/2], proof, tree.Root(), wealdtechHashType{}, nil)
		if err != nil {
			b.Fatal(err)
		}
		if !ok {
			b.Fatal("verification failed")
		}
	}
}
