## 성능개선

### lazy import
```js
// 전
import Detail from './routes/Detail.js'
import Cart from './routes/Cart.js'

// 후
import {lazy, Suspense, useEffect, useState} from 'react'

const Detail = lazy( () => import('./routes/Detail.js') )
const Cart = lazy( () => import('./routes/Cart.js') )

return(
  <Suspense fallback={ <div>로딩중임</div> }>
    <Detail shoes={shoes} />
  </Suspense>
)
```