import React from 'react';
import ListItem from '@material-ui/core/ListItem';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import ListItemText from '@material-ui/core/ListItemText';
import DashboardIcon from '@material-ui/icons/Dashboard';
import PeopleIcon from '@material-ui/icons/People';
import SubscriptionsIcon from '@material-ui/icons/Subscriptions';
import BookmarkIcon from '@material-ui/icons/Bookmark';

export const mainListItems = (
  <div>
    <ListItem button>
      <ListItemIcon style={{color: 'white'}}>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </ListItem>
    <ListItem button>
      <ListItemIcon  style={{color: 'white'}}>
        <PeopleIcon />
      </ListItemIcon>
      <ListItemText primary="Users" />
    </ListItem>

    <ListItem button>
      <ListItemIcon  style={{color: 'white'}}>
        <SubscriptionsIcon />
      </ListItemIcon>
      <ListItemText primary="Subscribers" />
    </ListItem>


    <ListItem button>
      <ListItemIcon  style={{color: 'white'}}>
        <BookmarkIcon />
      </ListItemIcon>
      <ListItemText primary="Publicaciones" />
    </ListItem>
    
  </div>
);


/*
export const secondaryListItems = (
  <div>
    <ListSubheader inset>Saved reports</ListSubheader>
    <ListItem button>
      <ListItemIcon>
        <AssignmentIcon />
      </ListItemIcon>
      <ListItemText primary="Current month" />
    </ListItem>
  </div>
);

*/