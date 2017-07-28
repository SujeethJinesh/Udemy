import React from 'react';
import ReactDOM from 'react-dom';

//importing components we made
import SearchBar from './components/search_bar'

//api key
const API_KEY='AIzaSyDgqQmQ7sKUtDWVCFyZJEzXEt-KWCmUf54'

// Create new component that makes some HTML
const App = () => {
    return (
        <div>
            <SearchBar />
        </div>
    );
}

// Take this HTML and put it on the page/DOM
ReactDOM.render(<App />, document.querySelector('.container'));
