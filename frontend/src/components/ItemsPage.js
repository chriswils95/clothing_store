import React , { useState, useEffect } from 'react';
import NavBar from './NavBar'
import ItemPage from './ItemPage'
import { Grid } from "@material-ui/core";


  export default function ItemsPage() {
    const [text, setText] = useState("Photos");
    const [auth, setAuth] = useState(true);
    const [images, setImages] = useState([]);
    
    
    
  useEffect(() => {
    const fetchData = async () => {
    try {
     const result = await fetch('api/items');
     const body = await result.json();
     setImages(body);
    } catch(err) {
      console.log("in here");
      // error handling code
    } 
  }

  // call the async fetchData function
  fetchData()

  }, [])

  useEffect(() => {
    // console.log(images);
  })
    
    return (
        <div>
         <NavBar text={text} auth={auth}/>
         <Grid container spacing={4}>
         {images.map(film => (
           <Grid item xs={12} sm={6} md={3}>
             <ItemPage category={film.master_category} item_id={film.item_id}/>
           </Grid>
          ))}
        </Grid>
      </div>
    );
  }