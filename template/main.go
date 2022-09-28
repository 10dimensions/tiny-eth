package main

import (
	"fmt"
	//"github.com/fatih/structs"
)


type Block struct {
	state map[string]*State
}

type State struct {
	balance uint64
}
  
var Blockchain = []*Block{}

func initialize() int{
	Blockchain = []*Block{}
	return len(Blockchain)
}

//Get block height
func getBlockHeight() int{
	return len(Blockchain)
}

//Add new block to chain
func addToChain(block Block){
	Blockchain=append(Blockchain,&block)
}

//Forge new block and archive the data
func set(address string, balance uint64){
	height := getBlockHeight()
	blockData := new(Block)
	if(height>0){
		blockData =  Blockchain[height-1]
	}
	
	archival_block_data := new(Block)
	archival_block_data.state = make(map[string]*State)

	//m := structs.Map(*blockData.state)
	m := blockData
	m.state = nil
	y := blockData.state
	m.state = y

	for k, v := range m.state { 
		archival_block_data.state[k] = &State{}
    archival_block_data.state[k].balance = v.balance
	}
		
	archival_block_data.state[address].balance = balance
	
	addToChain(*archival_block_data)
}
	
//Get block at height
func getBlockData(height int) *Block{
	return Blockchain[height]
}
	
//Get balance at given block height
func get(address string, height int) uint64{
	blockData := getBlockData(height)

	if value, ok := blockData.state[address]; ok {
			return value.balance
	} else {
			return 0
	}
}

func main(){
	status := initialize()
  fmt.Println(status)

  //Make txns
  set("A", 1)
  set("B", 2)
  set("A", 3)
  
  //Read txns
  fmt.Println(get("A", 0))
  fmt.Println(get("B", 0))
  fmt.Println(get("B", 1))
  fmt.Println(get("A", 1))
  fmt.Println(get("B", 2))
  fmt.Println(get("A", 2))
}