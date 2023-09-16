import React, { useEffect } from 'react';
import { View, Text, Button, StyleSheet } from 'react-native';

const ProfilePage = ({ navigation }) => {
  useEffect(() => {
    console.log('ProfilePage mounted');
    return () => {
      console.log('ProfilePage unmounted');
    };
  }, []);

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Profile Page</Text>
      <Button title="Go Back" onPress={() => navigation.goBack()} />
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    padding: 16,
  },
  title: {
    fontSize: 24,
    marginBottom: 16,
  },
});

export default ProfilePage;
