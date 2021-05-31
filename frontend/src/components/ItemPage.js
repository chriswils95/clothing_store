import React , { useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Card from '@material-ui/core/Card';
import CardActionArea from '@material-ui/core/CardActionArea';
import CardActions from '@material-ui/core/CardActions';
import CardMedia from '@material-ui/core/CardMedia';
import Button from '@material-ui/core/Button';
import NavBar from './NavBar'

const useStyles = makeStyles({
    root: {
      maxWidth: 345,
      minWidth: 200,
      "&:hover": {
        boxShadow: "-1px 10px 29px 0px rgba(0,0,0,0.8)"
    }
    },
    media: {
      height: 200,
    },
  });
  

  export default function ItemPage(props) {
    const classes = useStyles();
    const [text, setText] = useState("Photos");
    const [auth, setAuth] = useState(true);

    return (
      <div>
      <Card className={classes.root}>
        <CardActionArea>
          <CardMedia
            className={classes.media}
            image={require("../flowers/" + props.category + "/" + props.item_id + '.jpg').default}
            title="1164"
          />
        </CardActionArea>
        <CardActions>
          <Button size="small" color="primary">
            Share
          </Button>
          <Button size="small" color="primary">
            Learn More
          </Button>
        </CardActions>
      </Card>
      </div>
    );
  }