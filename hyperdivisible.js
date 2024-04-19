#!/usr/bin/env node

function findFactors(product) {
    let factors = [];
    for (let factor = 1; factor < product; factor++) {
        if (product % factor === 0) {
            factors.push(factor);
        }
    }
    return factors;
}

const MAX = 5040;
let histogram = {};

for (let product = 1; product <= MAX; product++) {
    const factors = findFactors(product);
    factorCount = factors.length + 1;
    if (!(factorCount in histogram)) {
        histogram[factorCount] = [];
    }
    histogram[factorCount].push(product);
    //console.log(`${product}: ${factors} (${factors.length} factors)`);
}

for (factorCount in histogram) {
    console.log(`${factorCount}: ${histogram[factorCount]}`);
}
