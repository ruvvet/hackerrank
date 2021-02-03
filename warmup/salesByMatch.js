function sockMerchant(n, ar) {
  const socks = ar.reduce((result, sock) => {
    if (result[sock]) {
      result[sock]++;
    } else {
      result[sock] = 1;
    }

    return result;
  }, {});

  const pairs = Object.values(socks).reduce(
    (pairs, color) => pairs + Math.floor(color / 2),
    0
  );
  return pairs;
}

sockMerchant(7, [1, 2, 1, 2, 1, 3, 2]);
