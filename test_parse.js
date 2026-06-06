const fs = require('fs');
const data = JSON.parse(fs.readFileSync('all_cards.json'));
let cards = [];
for (let set in data) {
    for (let c of data[set]) {
        if (c.name.includes('Bogus')) continue; // there's a "Bogus Card" in the json
        let types = ['Action']; // default
        if (c.is_attack) types.push('Attack');
        if (c.is_reaction) types.push('Reaction');
        if (c.treasure > 0) { types.push('Treasure'); types = types.filter(t=>t!=='Action'); }
        if (c.victory_points > 0) { types.push('Victory'); types = types.filter(t=>t!=='Action'); }
        
        cards.push({
            name: c.name,
            cost: c.cost_treasure || 0,
            types: types,
            set: set
        });
    }
}
console.log(`Parsed ${cards.length} cards. First few:`);
console.log(cards.slice(0, 5));
