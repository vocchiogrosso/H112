import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import HomePage from '../pages/HomePage';
import ProfilePage from '../pages/ProfilePage';

export type RootStackParamList = {
  Home: undefined;
  Profile: undefined;
};

const Stack = createStackNavigator<RootStackParamList>();

const RootNavigator = () => {
  return (
    <Stack.Navigator initialRouteName="Home">
      <Stack.Screen name="Home" component={HomePage} options={{ title: 'Home Page' }} />
      <Stack.Screen name="Profile" component={ProfilePage} options={{ title: 'Profile Page' }} />
    </Stack.Navigator>
  );
};

export default RootNavigator;
