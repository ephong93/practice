const { Carousel, Icon } = antd
const { useRef } = React;


function App() {
  const carouselRef = useRef(null);
  
  const next = () => {
    carouselRef.current.next();
  }
  
  return (
    <div className='app'>
      <h1>Carousel loop</h1>
      <div className='carousel-container'>
        <span className='button-left' onClick={() => carouselRef.current.prev()}>Left</span>
        <span className='button-right' onClick={() => carouselRef.current.next()}>Right</span>
        <Carousel
          dots={false}
          ref={carouselRef}
          style={{
            backgroundColor: '#55ddff',
            height: '200px'}}
          >
          <div>
            <div className='carousel-content'>
              A
            </div>
          </div>
          <div>
            <div className='carousel-content'>
              B
            </div>
          </div>
          <div>
            <div className='carousel-content'>
              C
            </div>
          </div>
        </Carousel>
      </div>
    </div>
  )
}
ReactDOM.render(<App />, document.getElementById('app'))
