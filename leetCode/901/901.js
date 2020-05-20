
var StockSpanner = function() {
  this.spans = []
  this.stockPrices = []
};

/**
 * @param {number} price
 * @return {number}
 */
StockSpanner.prototype.next = function(price) {
  let count = 1
  while (this.stockPrices.length > 0 && price >= this.stockPrices[this.stockPrices.length - 1]) {
    this.stockPrices.pop()
    count += this.spans.pop()
  }
  this.stockPrices.push(price)
  this.spans.push(count)
  return count
};

var obj = new StockSpanner()
var param_1 = obj.next(10)

/**
 * Your StockSpanner object will be instantiated and called as such:
 * var obj = new StockSpanner()
 * var param_1 = obj.next(price)
 */